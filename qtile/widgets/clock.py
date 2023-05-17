import subprocess


from datetime import datetime, timezone
from qtile_extras.widget import Clock
from qtile_extras.widget.mixins import TooltipMixin

class ClockTooltip(Clock, TooltipMixin):
    def __init__(self, *args, **kwargs):
        Clock.__init__(self, *args, **kwargs)
        TooltipMixin.__init__(self)
        self.add_defaults(Clock.defaults)
        self.add_defaults(TooltipMixin.defaults)
        # self.timeout_add(3600, self.tooltip_poll)
        self.tooltip_poll()
        # self.tooltip_text = self.tooltip_poll()

    def tooltip_poll(self):
        self.tooltip_text = subprocess.check_output(['cal']).decode().rstrip("\n")

    def poll(self):
        self.tooltip_poll()
        if self.timezone:
            now = datetime.now(timezone.utc).astimezone(self.timezone)
        else:
            now = datetime.now(timezone.utc).astimezone()
        return (now + self.DELTA).strftime(self.format)
