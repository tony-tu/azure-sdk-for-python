# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class PowerShellCommandResult(Model):
    """PowerShellCommandResult.

    :param message_type: the type of message
    :type message_type: int
    :param foreground_color: the HTML color string representing the
     foreground color.
    :type foreground_color: str
    :param background_color: the HTML color string representing the
     background color.
    :type background_color: str
    :param value: actual result text from the PowerShell Command
    :type value: str
    :param prompt: The interactive prompt message
    :type prompt: str
    :param exit_code: the exit code from a executable that was called from
     powershell.
    :type exit_code: int
    :param id: ID of the prompt message
    :type id: int
    :param caption: text that precedes the prompt.
    :type caption: str
    :param message: text of the prompt.
    :type message: str
    :param descriptions: collection of PromptFieldDescription objects that
     contains the user input
    :type descriptions: list of :class:`PromptFieldDescription
     <azure.mgmt.servermanager.models.PromptFieldDescription>`
    """ 

    _attribute_map = {
        'message_type': {'key': 'messageType', 'type': 'int'},
        'foreground_color': {'key': 'foregroundColor', 'type': 'str'},
        'background_color': {'key': 'backgroundColor', 'type': 'str'},
        'value': {'key': 'value', 'type': 'str'},
        'prompt': {'key': 'prompt', 'type': 'str'},
        'exit_code': {'key': 'exitCode', 'type': 'int'},
        'id': {'key': 'id', 'type': 'int'},
        'caption': {'key': 'caption', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
        'descriptions': {'key': 'descriptions', 'type': '[PromptFieldDescription]'},
    }

    def __init__(self, message_type=None, foreground_color=None, background_color=None, value=None, prompt=None, exit_code=None, id=None, caption=None, message=None, descriptions=None):
        self.message_type = message_type
        self.foreground_color = foreground_color
        self.background_color = background_color
        self.value = value
        self.prompt = prompt
        self.exit_code = exit_code
        self.id = id
        self.caption = caption
        self.message = message
        self.descriptions = descriptions
