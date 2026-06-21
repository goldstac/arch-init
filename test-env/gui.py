import sys
import subprocess
import threading
import os
import gi

gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')

from gi.repository import Gtk, Adw, Gio, GdkPixbuf, GLib


class ArchInitWindow(Gtk.ApplicationWindow):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.set_title("Arch Init")
        self.set_default_size(550, 450)
        self.pulse_timeout_id = None

        icon_path = "src/icon.png"
        if os.path.exists(icon_path):
            try:
                pixbuf = GdkPixbuf.Pixbuf.new_from_file(icon_path)
                self.set_icon_name(None)
                texture = GdkPixbuf.Texture.new_for_pixbuf(pixbuf)
            except Exception as e:
                print(f"Could not load icon: {e}")

        header_bar = Adw.HeaderBar()
        self.set_titlebar(header_bar)

        title_widget = Adw.WindowTitle(title="Arch Init", subtitle="By Li Productions")
        header_bar.set_title_widget(title_widget)

        main_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=0)
        self.set_child(main_box)

        content_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=18)
        content_box.set_margin_top(24)
        content_box.set_margin_bottom(24)
        content_box.set_margin_start(24)
        content_box.set_margin_end(24)
        main_box.append(content_box)

        welcome_label = Gtk.Label(
            label="Select an installation profile to configure your system."
        )
        welcome_label.add_css_class("body")
        content_box.append(welcome_label)

        preferences_group = Adw.PreferencesGroup()
        content_box.append(preferences_group)

        self.base_row = Adw.ActionRow(
            title="Base Profile",
            subtitle="Git, YAY, Fastfetch, Base-Devel, VS Code (OSS)",
        )
        preferences_group.add(self.base_row)

        self.base_button = Gtk.Button(label="Install")
        self.base_button.add_css_class("suggested-action")
        self.base_button.set_valign(Gtk.Align.CENTER)
        self.base_button.connect("clicked", self.on_base_clicked)
        self.base_row.add_suffix(self.base_button)

        self.medium_row = Adw.ActionRow(
            title="Medium Profile",
            subtitle="Adds VLC, Neovim, and core productivity utilities",
        )
        preferences_group.add(self.medium_row)

        self.medium_button = Gtk.Button(label="Install")
        self.medium_button.add_css_class("suggested-action")
        self.medium_button.set_valign(Gtk.Align.CENTER)
        self.medium_button.connect("clicked", self.on_medium_clicked)
        self.medium_row.add_suffix(self.medium_button)

        # Progress Bar Setup (Hidden by default until install begins)
        self.progress_bar = Gtk.ProgressBar()
        self.progress_bar.set_opacity(0.0)
        self.progress_bar.set_margin_top(10)
        content_box.append(self.progress_bar)

    def on_pulse_timeout(self):
        # Keeps the loading block moving back and forth smoothly
        self.progress_bar.pulse()
        return True

    def run_script_worker(self, script_path, button):
        subprocess.run(f"chmod +x {script_path} && ./{script_path}", shell=True)
        GLib.idle_add(self.reset_ui, button)

    def start_installation(self, script_path, button):
        button.set_label("Installing...")
        self.base_button.set_sensitive(False)
        self.medium_button.set_sensitive(False)
        
        # Show the progress bar
        self.progress_bar.set_opacity(1.0)
        
        # Start the progress bar animation loop every 100 milliseconds
        self.pulse_timeout_id = GLib.timeout_add(100, self.on_pulse_timeout)

        # Run the installation script in a separate thread to prevent UI freezing
        thread = threading.Thread(
            target=self.run_script_worker, 
            args=(script_path, button)
        )
        thread.start()

    def reset_ui(self, button):
        # Stop the progress bar animation loop
        if self.pulse_timeout_id:
            GLib.source_remove(self.pulse_timeout_id)
            self.pulse_timeout_id = None
        
        # Hide the progress bar and restore buttons
        self.progress_bar.set_opacity(0.0)
        self.progress_bar.set_fraction(0.0)
        
        button.set_label("Install")
        self.base_button.set_sensitive(True)
        self.medium_button.set_sensitive(True)
        return False

    def on_base_clicked(self, button):
        self.start_installation("src/templates-shell/base.sh", button)

    def on_medium_clicked(self, button):
        self.start_installation("src/templates-shell/medium.sh", button)


class ArchInitApp(Adw.Application):

    def __init__(self, **kwargs):
        super().__init__(
            application_id="com.liproductions.archinit",
            flags=Gio.ApplicationFlags.FLAGS_NONE,
            **kwargs,
        )

    def do_activate(self):
        win = ArchInitWindow(application=self)
        win.present()


if __name__ == "__main__":
    app = ArchInitApp()
    sys.exit(app.run(sys.argv))
