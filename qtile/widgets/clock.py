import subprocess

from qtile_extras.widget import Clock
from qtile_extras.widget.mixins import TooltipMixin

class ClockTooltip(Clock, TooltipMixin):
    def __init__(self, *args, **kwargs):
        Clock.__init__(self, *args, **kwargs)
        TooltipMixin.__init__(self)
        self.add_defaults(Clock.defaults)
        self.add_defaults(TooltipMixin.defaults)
        # self.tooltip_font = "NotoSans Mono"
        # self.tooltip_fontsize = 18

        self.tooltip_text = self.tooltip_poll()

    def tooltip_poll(self):
        return subprocess.check_output(['cal']).decode().lstrip("\n")
