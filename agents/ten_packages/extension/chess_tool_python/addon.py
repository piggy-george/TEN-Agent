#
#
# Agora Real Time Engagement
# Created by Tomas Liu in 2024-08.
# Copyright (c) 2024 Agora IO. All rights reserved.
#
#
from ten import (
    Addon,
    register_addon_as_extension,
    TenEnv,
)


@register_addon_as_extension("chess_tool_python")
class ChessToolExtensionAddon(Addon):

    def on_create_instance(self, ten_env: TenEnv, name: str, context) -> None:
        from .extension import ChessToolExtension
        from .log import logger
        logger.info("ChessToolExtensionAddon on_create_instance")
        ten_env.on_create_instance_done(ChessToolExtension(name), context)
