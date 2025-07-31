# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import json
import os
from uuid import uuid4

from digitalhub.entities.function.crud import get_function
from digitalhub.entities.workflow.crud import get_workflow
from digitalhub.runtimes.enums import RuntimeEnvVar
from digitalhub.stores.credentials.enums import CredsEnvVar
from hera.workflows import DAG, Artifact, Container, Parameter, Steps, Task, Step
from hera.workflows import models as m
from hera.workflows._context import _context


def step(**step_kwargs) -> Task:
    """
    Create a step from a container template and function name.

    Parameters
    ----------
    **step_kwargs : dict
        Keyword arguments for the container template. Accepts inputs, name,
        function, workflow, and other parameters for task configuration.

    Returns
    -------
    Task
        A Hera task object configured with the specified container template
        and parameters.

    Raises
    ------
    ValueError
        If called outside of a DAG or Steps context.
    """
    inner_ctx = _context.pieces[-1]
    if isinstance(inner_ctx, DAG):
        op_type = "dag-op-"
    elif isinstance(inner_ctx, Steps):
        op_type = "step-op-"
    else:
        raise ValueError("step() can only be called inside a DAG or Steps")
    _context.pieces = _context.pieces[:-1]

    inputs = step_kwargs.pop("inputs", None)
    if inputs is not None:
        step_kwargs["inputs"] = [k for k in inputs.keys()]
    container = container_template(**step_kwargs)

    _context.pieces.append(inner_ctx)

    name = op_type
    if (kwarg_name := step_kwargs.get("name")) is not None:
        name += kwarg_name + "-"
    elif (func := step_kwargs.get("function")) is not None:
        name += func + "-"
    elif (wkfl := step_kwargs.get("workflow")) is not None:
        name += wkfl + "-"
    name += uuid4().hex[:8]

    # If the inner context is a DAG, return a Task; otherwise, return a Step
    if isinstance(inner_ctx, DAG):
        return Task(name=name, template=container, arguments=inputs)
    return Step(name=name, template=container, arguments=inputs)


def container_template(
    template: dict,
    function: str | None = None,
    function_id: str | None = None,
    workflow: str | None = None,
    workflow_id: str | None = None,
    name: str | None = None,
    inputs: list | None = None,
    outputs: list | None = None,
    **kwargs,
) -> Container:
    """
    Create a Hera container template for workflow execution.

    Parameters
    ----------
    template : dict
        Parameters template to pass to function.run() or workflow.run().
    function : str, optional
        Function name to execute.
    function_id : str, optional
        Unique identifier for the function.
    workflow : str, optional
        Workflow name to execute.
    workflow_id : str, optional
        Unique identifier for the workflow.
    name : str, optional
        Custom name for the step.
    inputs : list, optional
        List of input parameter names for the step.
    outputs : list, optional
        List of output parameter names for the step.
    **kwargs
        Additional keyword arguments passed to the container configuration.

    Returns
    -------
    Container
        A Hera container template configured with the specified entity,
        inputs, outputs, and execution parameters.

    Raises
    ------
    RuntimeError
        If neither function nor workflow is provided, if the specified
        entity is not found, or if the workflow image environment
        variable is not set.
    """

    cmd = ["python"]
    args = ["step.py"]

    # Add entity
    try:
        project = os.environ.get(RuntimeEnvVar.PROJECT.value)
        if function is not None:
            exec_entity = get_function(function, project=project, entity_id=function_id)
        elif workflow is not None:
            exec_entity = get_workflow(workflow, project=project, entity_id=workflow_id)
        else:
            raise RuntimeError("Either function or workflow must be provided.")
    except Exception as e:
        raise RuntimeError("Function or workflow not found.") from e
    args.extend(["--entity", str(exec_entity.key)])

    # Add kwargs
    template["wait"] = True
    args.extend(["--kwargs", json.dumps(template, cls=PipelineParamEncoder)])

    # Get image stepper
    image = os.environ.get(CredsEnvVar.DHCORE_WORKFLOW_IMAGE.value)
    if image is None:
        raise RuntimeError(f"Env var '{CredsEnvVar.DHCORE_WORKFLOW_IMAGE.value}' is not set")

    # Get step outputs
    outputs = outputs if outputs is not None else []
    step_outputs = []
    for o in outputs:
        path = "/tmp/entity_" + str(o).replace(".", "_").replace("/", "_")
        step_outputs.append(Artifact(name=o, path=path))
        step_outputs.append(Parameter(name=o, value_from=m.ValueFrom(path=path), output=True))

    # Get step inputs
    inputs = inputs if inputs is not None else []
    step_inputs = [Parameter(name=i) for i in inputs]

    # Get step name
    cont_name = "container-"
    if name is not None:
        cont_name += name + "-"
    cont_name += exec_entity.name + "-" + str(uuid4().hex[:8])

    return Container(
        name=cont_name,
        image=image,
        command=cmd,
        args=args,
        outputs=step_outputs,
        inputs=step_inputs,
    )


class PipelineParamEncoder(json.JSONEncoder):
    """
    Custom JSON encoder for pipeline parameters.

    Extends json.JSONEncoder to handle Parameter objects by encoding
    their value attribute instead of the full object.
    """

    def default(self, obj):
        """
        Override default method to handle Parameter objects.

        Parameters
        ----------
        obj : any
            Object to encode.

        Returns
        -------
        any
            The object's value if it's a Parameter, otherwise defers
            to the parent class default method.
        """
        if isinstance(obj, Parameter):
            return obj.value
        return super().default(obj)
