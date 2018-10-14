"""Decorator functions to use when creating skill modules."""

import logging

from opsdroid.const import REGEX_SCORE_FACTOR
from opsdroid.helper import get_opsdroid
from opsdroid.web import Web


_LOGGER = logging.getLogger(__name__)


def match_regex(regex, case_sensitive=True, score_factor=None):
    """Return regex match decorator.

    Args:
        regex (str): The regular expression to match.
        case_sensitive (bool, optional): Whether or not ignore the matching
            case. Defaults to True.
        score_factor (float, optional): The factor (0 to 1) to use when the
            regex is used over a Natural Language Understanding (NLU) skill.
            Defaults to None, but only to use the default value of 0.6 defined
            in REGEX_SCORE_FACTOR.

    Returns:
        A regex match decorator.
    """
    def matcher(func):
        """Add decorated function to skills list for regex matching."""
        opsdroid = get_opsdroid()
        if opsdroid:
            config = opsdroid.loader.current_import_config
            regex_setup = {
                "expression": regex,
                "case_sensitive": case_sensitive,
                "score_factor": score_factor or REGEX_SCORE_FACTOR,
            }
            opsdroid.skills.append({"regex": regex_setup,
                                    "skill": func,
                                    "config": config})
        return func
    return matcher


def match_apiai_action(action):
    """Return Dialogflow action match decorator.

    Args:
        action (str): It is a single word (ID) created in Dialogflow once the
            training phrases for each intent are built.

    Returns:
        A dialogflow action match decorator.
    """
    def matcher(func):
        """Add decorated function to skills list for Dialogflow matching."""
        opsdroid = get_opsdroid()
        if opsdroid:
            config = opsdroid.loader.current_import_config
            opsdroid.skills.append({"dialogflow_action": action,
                                    "skill": func,
                                    "config": config})
        return func
    _LOGGER.warning(_("Api.ai is now called Dialogflow, this matcher "
                      "will stop working in the future. "
                      "Use match_dialogflow_action instead."))
    return matcher


def match_apiai_intent(intent):
    """Return Dialogflow intent match decorator.

    Args:
        intent (str): It is a single word (ID) defined in the Dialogflow agent
            that maps user input to responses.

    Returns:
        A dialogflow intent match decorator.
    """
    def matcher(func):
        """Add decorated function to skills list for Dialogflow matching."""
        opsdroid = get_opsdroid()
        if opsdroid:
            config = opsdroid.loader.current_import_config
            opsdroid.skills.append({"dialogflow_intent": intent,
                                    "skill": func,
                                    "config": config})
        return func
    _LOGGER.warning(_("Api.ai is now called Dialogflow, this matcher "
                      "will stop working in the future. "
                      "Use match_dialogflow_intent instead."))
    return matcher


def match_dialogflow_action(action):
    """Return Dialogflow action match decorator.

    Args:
        action (str): It is a single word (ID) created in Dialogflow once the
            training phrases for each intent are built.

    Returns:
        A dialogflow action match decorator.
    """
    def matcher(func):
        """Add decorated function to skills list for Dialogflow matching."""
        opsdroid = get_opsdroid()
        if opsdroid:
            config = opsdroid.loader.current_import_config
            opsdroid.skills.append({"dialogflow_action": action,
                                    "skill": func,
                                    "config": config})
        return func
    return matcher


def match_dialogflow_intent(intent):
    """Return Dialogflow intent match decorator.

    Args:
        intent (str): It is a single word (ID) defined in the Dialogflow agent
            that maps user input to responses.

    Returns:
        A dialogflow intent match decorator.
    """
    def matcher(func):
        """Add decorated function to skills list for Dialogflow matching."""
        opsdroid = get_opsdroid()
        if opsdroid:
            config = opsdroid.loader.current_import_config
            opsdroid.skills.append({"dialogflow_intent": intent,
                                    "skill": func,
                                    "config": config})
        return func
    return matcher


def match_luisai_intent(intent):
    """Return luisai intent match decorator.

    Args:
        intent (str): It is a single word (ID) defined in the LUIS service
            that maps user input to responses.

    Returns:
        A luisai intent match decorator.
    """
    def matcher(func):
        """Add decorated function to skills list for luisai matching."""
        opsdroid = get_opsdroid()
        if opsdroid:
            config = opsdroid.loader.current_import_config
            opsdroid.skills.append({"luisai_intent": intent,
                                    "skill": func,
                                    "config": config})
        return func
    return matcher


def match_rasanlu(intent):
    """Return Rasa NLU intent match decorator.

    Args:
        intent (str): It is a single word (ID) defined in Rasa NLU service
            that maps user input to responses.

    Returns:
        A luisai intent match decorator.
    """
    def matcher(func):
        """Add decorated function to skills list for Rasa NLU matching."""
        opsdroid = get_opsdroid()
        if opsdroid:
            config = opsdroid.loader.current_import_config
            opsdroid.skills.append({"rasanlu_intent": intent,
                                    "skill": func,
                                    "config": config})
        return func
    return matcher


def match_recastai(intent):
    """Return recastai intent match decorator.

    Args:
        intent (str): It is a single word (ID) defined in Recast AI service
            that maps user input to responses.

    Returns:
        A recastai intent match decorator.
    """
    def matcher(func):
        """Add decorated function to skills list for recastai matching."""
        opsdroid = get_opsdroid()
        if opsdroid:
            config = opsdroid.loader.current_import_config
            opsdroid.skills.append({"recastai_intent": intent,
                                    "skill": func,
                                    "config": config})
        return func
    return matcher


def match_witai(intent):
    """Return witai intent match decorator.

    Args:
        intent (str): It is a single word (ID) defined in Wit AI service
            that maps user input to responses.

    Returns:
        A witai intent match decorator.
    """
    def matcher(func):
        """Add decorated function to skills list for witai matching."""
        opsdroid = get_opsdroid()
        if opsdroid:
            config = opsdroid.loader.current_import_config
            opsdroid.skills.append({"witai_intent": intent,
                                    "skill": func,
                                    "config": config})
        return func
    return matcher


def match_crontab(crontab, timezone=None):
    """Return crontab match decorator.

    Args:
        crontab (str): Cron timing (min, hour, day of the month, month, day of
            the week) that will trigger the matcher. Examples: '* * * * *'
            triggers every minute. '0 2 * * 0' triggers every Sun at 2:00am.
        timezone (str): Timezone to use.  Defaults to None, but when None is
            defined uses UTC.

    Returns:
        A crontab match timer decorator.
    """
    def matcher(func):
        """Add decorated function to skills list for crontab matching."""
        opsdroid = get_opsdroid()
        if opsdroid:
            config = opsdroid.loader.current_import_config
            opsdroid.skills.append({"crontab": crontab,
                                    "skill": func,
                                    "config": config,
                                    "timezone": timezone})
        return func
    return matcher


def match_webhook(webhook):
    """Return webhook match decorator.

    Args:
        webhook (str): The webhook name to enable.
            (http(s)://domain:port/skill/<name>/webhook).

    Returns:
        A webhook match decorator.
    """
    def matcher(func):
        """Add decorated function to skills list for webhook matching."""
        opsdroid = get_opsdroid()
        if opsdroid:
            config = opsdroid.loader.current_import_config
            opsdroid.skills.append({"webhook": webhook,
                                    "skill": func,
                                    "config": config})

            async def wrapper(req, opsdroid=opsdroid, config=config):
                """Wrap up the aiohttp handler."""
                _LOGGER.info("Running skill %s via webhook", webhook)
                opsdroid.stats["webhooks_called"] = \
                    opsdroid.stats["webhooks_called"] + 1
                await func(opsdroid, config, req)
                return Web.build_response(200, {"called_skill": webhook})

            opsdroid.web_server.web_app.router.add_post(
                "/skill/{}/{}".format(config["name"], webhook), wrapper)
            opsdroid.web_server.web_app.router.add_post(
                "/skill/{}/{}/".format(config["name"], webhook), wrapper)

        return func
    return matcher


def match_always(func=None):
    """Return always match decorator.

    This matcher parses every message as it is always running.

    Args:
        func (func): Receives a function. Defaults to None.

    Returns:
        An always match decorator.
    """
    def matcher(func):
        """Add decorated function to skills list for always matching."""
        opsdroid = get_opsdroid()
        if opsdroid:
            config = opsdroid.loader.current_import_config
            opsdroid.skills.append({"always": True,
                                    "skill": func,
                                    "config": config})
        return func

    # Allow for decorator with or without parenthesis as there are no args.
    if callable(func):
        return matcher(func)
    return matcher
