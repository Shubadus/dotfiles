import math
import subprocess

import psutil

from pathlib import Path

from libqtile import bar, configurable, images
from libqtile.widget import base
from qtile_extras.widget.mixins import TooltipMixin


BATTERY_ICONS = {
    'Charging': {
        '100': '',
        '90': '',
        '80': '',
        '70': '',
        '60': '',
        '50': '',
        '40': '',
        '30': '',
        '20': '',
        '10': '',
        '0': ''
    },
    'Discharging': {
        '100': '',
        '90': '',
        '80': '',
        '70': '',
        '60': '',
        '50': '',
        '40': '',
        '30': '',
        '20': '',
        '10': '',
        '0': ''
    },
    'Full': {
        '100': ''
    }
}
PRIMARY_BATTERY= list(Path('/sys/class/power_supply/').glob('BAT*'))[0]
POWER_PROFILES = (
    'balanced',
    'performance',
    'power-saver'
)


class BatteryIcon(base._Widget):
    """Battery life indicator widget."""

    orientations = base.ORIENTATION_HORIZONTAL
    defaults: list[tuple[str, Any, str]] = [
        ("battery", 0, "Which battery should be monitored"),
        ("update_interval", 60, "Seconds between status updates"),
        ("theme_path", default_icon_path(), "Path of the icons"),
        ("scale", 1, "Scale factor relative to the bar height.  " "Defaults to 1"),
    ]

    icon_names = (
        "battery-missing",
        "battery-caution",
        "battery-low",
        "battery-good",
        "battery-full",
        "battery-caution-charging",
        "battery-low-charging",
        "battery-good-charging",
        "battery-full-charging",
        "battery-full-charged",
    )

    def __init__(self, **config) -> None:
        if "update_delay" in config:
            warnings.warn(
                "Change from using update_delay to update_interval for battery widget, removed in 0.15",
                DeprecationWarning,
            )
            config["update_interval"] = config.pop("update_delay")

        base._Widget.__init__(self, length=bar.CALCULATED, **config)
        self.add_defaults(self.defaults)
        self.scale: float = 1.0 / self.scale

        self.length_type = bar.STATIC
        self.length = 0
        self.image_padding = 0
        self.images: dict[str, Img] = {}
        self.current_icon = "battery-missing"

        self._battery = self._load_battery(**config)

    @staticmethod
    def _load_battery(**config):
        """Function used to load the Battery object

        Battery behavior can be changed by overloading this function in a base
        class.
        """
        return load_battery(**config)

    def timer_setup(self) -> None:
        self.update()
        self.timeout_add(self.update_interval, self.timer_setup)

    def _configure(self, qtile, bar) -> None:
        base._Widget._configure(self, qtile, bar)
        self.image_padding = 0
        self.setup_images()
        self.image_padding = (self.bar.height - self.bar.height / 5) / 2

    def setup_images(self) -> None:
        d_imgs = images.Loader(self.theme_path)(*self.icon_names)

        new_height = self.bar.height * self.scale - self.image_padding
        for key, img in d_imgs.items():
            img.resize(height=new_height)
            if img.width > self.length:
                self.length = int(img.width + self.image_padding * 2)
            self.images[key] = img

    def update(self) -> None:
        status = self._battery.update_status()
        icon = self._get_icon_key(status)
        if icon != self.current_icon:
            self.current_icon = icon
            self.draw()

    def draw(self) -> None:
        self.drawer.clear(self.background or self.bar.background)
        image = self.images[self.current_icon]
        self.drawer.ctx.save()
        self.drawer.ctx.translate(0, (self.bar.height - image.height) // 2)
        self.drawer.ctx.set_source(image.pattern)
        self.drawer.ctx.paint()
        self.drawer.ctx.restore()
        self.drawer.draw(offsetx=self.offset, offsety=self.offsety, width=self.length)

    @staticmethod
    def _get_icon_key(status: BatteryStatus) -> str:
        key = "battery"

        percent = status.percent
        if percent < 0.2:
            key += "-caution"
        elif percent < 0.4:
            key += "-low"
        elif percent < 0.8:
            key += "-good"
        else:
            key += "-full"

        state = status.state
        return key
# class Battery(base._TextBox, base.PaddingMixin, base.MarginMixin):
#     def __init__(self, **config):
#         base._TextBox.__init__(self, **config)
#         bat = psutil.sensors_battery()
#         self.add_defaults(base._TextBox.defaults)
#         self.add_defaults(base.PaddingMixin.defaults)
#         self.add_defaults(base.MarginMixin.defaults)
#         self.battery = dict(
#             health = self.get_battery_health(),
#             name = PRIMARY_BATTERY.name,
#             path = PRIMARY_BATTERY,
#             percent = int(bat.percent),
#             profile = self.get_current_power_plan(),
#             status = PRIMARY_BATTERY.joinpath('status').read_text().strip('\n'),
#             time_left = self.secs2hours(bat.secsleft)
#         )
#         self.bat_percent_icon = str(math.floor(self.battery.percent/10)*10)
#
#     def _configure(self, qtile, bar):
#         base._TextBox._configure(self, qtile, bar)
#
#     def box_width(self):
#         width, _ = self.drawer.max_layout_size([
#             self.fmt.format(self.text)
#         ], self.font, self.fontsize)
#         return width + self.padding_x * 2
#
#     def calculate_length(self):
#         if self.text:
#             return self.size
#         else:
#             return 0
#
#     def drawbox(self, offset, text, bordercolor, textcolor, width=None, rounded=False):
#         self.layout.text = self.fmt.format(text)
#         self.layout.font_family = self.font
#         self.layout.font_size = self.fontsize
#         self.layout.colour = textcolor
#         if width is not None:
#             self.layout.width = width
#
#         framed = self.layout.framed(0, bordercolor, 0, self.padding_y, textcolor)
#         x = offset
#         y = (self.bar.height - framed.height) // 2
#         # w = framed.width
#         w = self.size - self.borderwidth * 2 - self.padding * 2
#         h = framed.height
#
#         if rounded:
#             self.drawer.set_source_rgb(self.selected or self.bar.background)
#             if self.value:
#                 self.drawer.rounded_fillrect(x, y, w * self.value, h, self.borderwidth)
#             self.drawer.set_source_rgb(self.background or self.bar.background)
#             self.drawer.rounded_rectangle(x, y, w, h, self.borderwidth)
#         else:
#             self.drawer.set_source_rgb(self.selected or self.bar.background)
#             if self.value:
#                 self.drawer.fillrect(x, y, w * self.value, h, self.borderwidth)
#             self.drawer.set_source_rgb(self.background or self.bar.background)
#             self.drawer.rectangle(x, y, w, h, self.borderwidth)
#
#         framed.draw(offset + w / 2 - framed.width / 2, y, rounded)
#
#     def draw(self):
#         self.drawer.clear(self.bar.background)
#
#         bw = self.box_width()
#         self.drawbox(
#             self.margin_x,
#             self.text,
#             self.background,
#             self.foreground,
#             width=bw,
#             rounded=self.rounded,
#         )
#         self.drawer.draw(offsetx=self.offset - self.width, offsety=self.offsety, width=self.width)
#
#     def get_power_status(self):
#         message = '\n'.join([
#             '{:<18} {}'.format('Name:', self.battery.name),
#             '{:<18} {}'.format('Status:', self.battery.status),
#             '{:<18} {}%'.format('Battery Percent:', self.battery.percent),
#             '{:<18} {}%'.format('Battery Health:', self.battery.health),
#             '{:<18} {}'.format('Power Profile:', self.battery.profile)
#         ])
#         if self.battery_status == "Discharging":
#             message += '\n{:18} {}'.format('Time Remaining:', self.battery.time_left)
#         return message
#
#     def get_battery_health(self):
#         orig_full_cap = int(self.battery.path.joinpath('charge_full_design').read_text())
#         full_cap = int(self.battery.path.joinpath('charge_full').read_text())
#         return int(full_cap / orig_full_cap * 100)
#
#     def get_current_power_plan(self):
#         return subprocess.check_output(['powerprofilesctl', 'get']).decode().strip("\n")
#
#     def set_power_plan(self, plan: str):
#         subprocess.call(['powerprofilesctl', 'set', plan]) 
#
#     def next_power_plan(self):
#         next_index = POWER_PROFILES.index(self.battery.profile) + 1
#         if next_index > len(POWER_PROFILES) - 1:
#             next_index = 0
#         self.set_power_plan(POWER_PROFILES[next_index])
#         self.battery.profile = self.get_current_power_plan()
#         self.send_notification(f'New Power Profile: {self.battery.profile}')
#
#     def send_notification(self, message: str):
#         """Send notification to system using libnotify"""
#         subprocess.call(['notify-send', '-r', '55555', '-u', 'normal', message])
#
