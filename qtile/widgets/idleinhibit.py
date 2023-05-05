# from libqtile.
from libqtile.widget import base

IDLE_ICONS = {
    'inhibited': '',
    'uninhibited': ''
}

# TODO: Implement poll function to check if SwayIdle (Or X equivalent) is active or not
# then call update passing the poll function.
class IdleInhibitor(base.PaddingMixin, base.MarginMixin, base._TextBox):
    def __init__(self, **config):
        base._TextBox.__init__(self, **config)
        self.add_defaults(base._TextBox.defaults)
        self.add_defaults(base.PaddingMixin.defaults)
        self.add_defaults(base.MarginMixin.defaults)

    def _configure(self, qtile, bar):
        base._TextBox._configure(self, qtile, bar)

    def box_width(self):
        width, _ = self.drawer.max_layout_size([
            self.fmt.format(self.text)
        ], self.font, self.fontsize)
        return width + self.padding_x * 2

    def calculate_length(self):
        if self.text:
            return self.size
        else:
            return 0

    def drawbox(self, offset, text, bordercolor, textcolor, width=None, rounded=False):
        self.layout.text = self.fmt.format(text)
        self.layout.font_family = self.font
        self.layout.font_size = self.fontsize
        self.layout.colour = textcolor
        if width is not None:
            self.layout.width = width

        framed = self.layout.framed(0, bordercolor, 0, self.padding_y, textcolor)
        x = offset
        y = (self.bar.height - framed.height) // 2
        # w = framed.width
        w = self.size - self.borderwidth * 2 - self.padding * 2
        h = framed.height

        if rounded:
            self.drawer.set_source_rgb(self.selected or self.bar.background)
            if self.value:
                self.drawer.rounded_fillrect(x, y, w * self.value, h, self.borderwidth)
            self.drawer.set_source_rgb(self.background or self.bar.background)
            self.drawer.rounded_rectangle(x, y, w, h, self.borderwidth)
        else:
            self.drawer.set_source_rgb(self.selected or self.bar.background)
            if self.value:
                self.drawer.fillrect(x, y, w * self.value, h, self.borderwidth)
            self.drawer.set_source_rgb(self.background or self.bar.background)
            self.drawer.rectangle(x, y, w, h, self.borderwidth)

        framed.draw(offset + w / 2 - framed.width / 2, y, rounded)

    def draw(self):
        self.drawer.clear(self.bar.background)

        bw = self.box_width()
        self.drawbox(
            self.margin_x,
            self.text,
            self.background,
            self.foreground,
            width=bw,
            rounded=self.rounded,
        )
        self.drawer.draw(offsetx=self.offset - self.width, offsety=self.offsety, width=self.width)
