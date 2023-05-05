from qtile_extras.widget import Memory
from qtile_extras.widget.mixins import TooltipMixin

class MemoryTooltip(Memory, TooltipMixin):
    def __init__(self, *args, **kwargs):
        Memory.__init__(self, *args, **kwargs)
        TooltipMixin.__init__(self)
        self.add_defaults(TooltipMixin.defaults)

        self.tooltip_text = self.poll()
