import tkinter as tk
from tkinter import messagebox, ttk

from circular_list import DoublyCircularLinkedList


class MusicPlayerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Circular Music Player")
        self.root.geometry("1050x700")
        self.root.minsize(900, 620)
        self.root.configure(bg="#10131b")

        self.playlist = DoublyCircularLinkedList()
        self.status_var = tk.StringVar(value="Ready. Add a track to get started.")

        self.setup_styles()
        self.build_interface()
        self.refresh_playlist()

    def setup_styles(self):
        style = ttk.Style()
        style.theme_use("clam")

        style.configure("App.TFrame", background="#10131b")
        style.configure("Panel.TFrame", background="#181d29")
        style.configure("Card.TFrame", background="#202738")
        style.configure(
            "Title.TLabel",
            background="#10131b",
            foreground="#f4f6fb",
            font=("Segoe UI", 23, "bold"),
        )
        style.configure(
            "Subtitle.TLabel",
            background="#10131b",
            foreground="#9ca8bd",
            font=("Segoe UI", 10),
        )
        style.configure(
            "Section.TLabel",
            background="#181d29",
            foreground="#f4f6fb",
            font=("Segoe UI", 11, "bold"),
        )
        style.configure(
            "Field.TLabel",
            background="#181d29",
            foreground="#c0c9d8",
            font=("Segoe UI", 9),
        )
        style.configure(
            "CardTitle.TLabel",
            background="#202738",
            foreground="#9ca8bd",
            font=("Segoe UI", 9, "bold"),
        )
        style.configure(
            "TrackTitle.TLabel",
            background="#202738",
            foreground="#ffffff",
            font=("Segoe UI", 17, "bold"),
            wraplength=260,
        )
        style.configure(
            "CardText.TLabel",
            background="#202738",
            foreground="#b7c2d6",
            font=("Segoe UI", 10),
        )
        style.configure(
            "Count.TLabel",
            background="#181d29",
            foreground="#70e1b0",
            font=("Segoe UI", 9, "bold"),
        )
        style.configure(
            "TEntry",
            fieldbackground="#252d3d",
            foreground="#f4f6fb",
            insertcolor="#ffffff",
            bordercolor="#354057",
            padding=8,
        )
        style.configure(
            "Treeview",
            background="#141a25",
            fieldbackground="#141a25",
            foreground="#dce3ef",
            borderwidth=0,
            rowheight=34,
            font=("Segoe UI", 10),
        )
        style.configure(
            "Treeview.Heading",
            background="#252d3d",
            foreground="#bfcadd",
            borderwidth=0,
            padding=(9, 10),
            font=("Segoe UI", 9, "bold"),
        )
        style.map(
            "Treeview",
            background=[("selected", "#313e56")],
            foreground=[("selected", "#ffffff")],
        )
        style.configure(
            "Primary.TButton",
            background="#70e1b0",
            foreground="#10131b",
            font=("Segoe UI", 10, "bold"),
            borderwidth=0,
            padding=(12, 10),
        )
        style.map("Primary.TButton", background=[("active", "#8af0c5")])
        style.configure(
            "Control.TButton",
            background="#2b3447",
            foreground="#f4f6fb",
            font=("Segoe UI", 10, "bold"),
            borderwidth=0,
            padding=(10, 10),
        )
        style.map("Control.TButton", background=[("active", "#3a4760")])
        style.configure(
            "Danger.TButton",
            background="#512c3a",
            foreground="#ffdce5",
            font=("Segoe UI", 10, "bold"),
            borderwidth=0,
            padding=(10, 10),
        )
        style.map("Danger.TButton", background=[("active", "#6a3449")])
        style.configure(
            "Status.TLabel",
            background="#10131b",
            foreground="#9ca8bd",
            font=("Segoe UI", 9),
        )

    def build_interface(self):
        outer = ttk.Frame(self.root, style="App.TFrame", padding=(24, 22, 24, 16))
        outer.pack(fill="both", expand=True)

        header = ttk.Frame(outer, style="App.TFrame")
        header.pack(fill="x")
        ttk.Label(header, text="CIRCULAR MUSIC PLAYER", style="Title.TLabel").pack(anchor="w")
        ttk.Label(
            header,
            text="A doubly circular playlist — move forward or backward without reaching an end.",
            style="Subtitle.TLabel",
        ).pack(anchor="w", pady=(4, 0))

        content = ttk.Frame(outer, style="App.TFrame")
        content.pack(fill="both", expand=True, pady=(22, 14))

        playlist_panel = ttk.Frame(content, style="Panel.TFrame", padding=17)
        playlist_panel.pack(side="left", fill="both", expand=True, padx=(0, 14))

        panel_header = ttk.Frame(playlist_panel, style="Panel.TFrame")
        panel_header.pack(fill="x", pady=(0, 13))
        ttk.Label(panel_header, text="YOUR PLAYLIST", style="Section.TLabel").pack(side="left")
        self.count_label = ttk.Label(panel_header, text="0 TRACKS", style="Count.TLabel")
        self.count_label.pack(side="right")

        tree_frame = ttk.Frame(playlist_panel, style="Panel.TFrame")
        tree_frame.pack(fill="both", expand=True)
        self.track_tree = ttk.Treeview(
            tree_frame,
            columns=("title", "artist", "duration"),
            show="headings",
            selectmode="browse",
        )
        self.track_tree.heading("title", text="TITLE")
        self.track_tree.heading("artist", text="ARTIST")
        self.track_tree.heading("duration", text="LENGTH")
        self.track_tree.column("title", width=230, minwidth=130, anchor="w")
        self.track_tree.column("artist", width=160, minwidth=100, anchor="w")
        self.track_tree.column("duration", width=75, minwidth=65, anchor="center")
        self.track_tree.tag_configure("current", background="#203b35", foreground="#8af0c5")
        self.track_tree.pack(side="left", fill="both", expand=True)

        scrollbar = ttk.Scrollbar(tree_frame, orient="vertical", command=self.track_tree.yview)
        scrollbar.pack(side="right", fill="y")
        self.track_tree.configure(yscrollcommand=scrollbar.set)
        self.track_tree.bind("<Double-1>", self.select_track)

        ttk.Label(
            playlist_panel,
            text="Double-click a track to make it the current track.",
            style="Subtitle.TLabel",
        ).pack(anchor="w", pady=(10, 0))

        side_panel = ttk.Frame(content, style="Panel.TFrame", padding=17, width=310)
        side_panel.pack(side="right", fill="y")
        side_panel.pack_propagate(False)

        ttk.Label(side_panel, text="CURRENT TRACK", style="Section.TLabel").pack(anchor="w")
        self.now_card = ttk.Frame(side_panel, style="Card.TFrame", padding=16)
        self.now_card.pack(fill="x", pady=(12, 19))
        ttk.Label(self.now_card, text="NOW SELECTED", style="CardTitle.TLabel").pack(anchor="w")
        self.current_title = ttk.Label(
            self.now_card, text="No track selected", style="TrackTitle.TLabel"
        )
        self.current_title.pack(anchor="w", pady=(10, 5))
        self.current_artist = ttk.Label(
            self.now_card, text="Add a track to your playlist", style="CardText.TLabel"
        )
        self.current_artist.pack(anchor="w")
        self.current_duration = ttk.Label(
            self.now_card, text="--:--", style="CardText.TLabel"
        )
        self.current_duration.pack(anchor="w", pady=(12, 0))

        ttk.Label(side_panel, text="PLAYBACK CONTROLS", style="Section.TLabel").pack(
            anchor="w", pady=(0, 10)
        )
        navigation = ttk.Frame(side_panel, style="Panel.TFrame")
        navigation.pack(fill="x")
        navigation.columnconfigure(0, weight=1)
        navigation.columnconfigure(1, weight=1)
        ttk.Button(
            navigation,
            text="Previous",
            command=self.previous_track,
            style="Control.TButton",
        ).grid(row=0, column=0, sticky="ew", padx=(0, 5))
        ttk.Button(
            navigation,
            text="Next",
            command=self.next_track,
            style="Control.TButton",
        ).grid(row=0, column=1, sticky="ew", padx=(5, 0))
        ttk.Button(
            side_panel,
            text="Delete Current Track",
            command=self.delete_current,
            style="Danger.TButton",
        ).pack(fill="x", pady=(10, 21))

        ttk.Label(side_panel, text="ADD A TRACK", style="Section.TLabel").pack(
            anchor="w", pady=(0, 10)
        )
        ttk.Label(side_panel, text="Track title", style="Field.TLabel").pack(anchor="w")
        self.title_entry = ttk.Entry(side_panel)
        self.title_entry.pack(fill="x", pady=(4, 10))

        ttk.Label(side_panel, text="Artist", style="Field.TLabel").pack(anchor="w")
        self.artist_entry = ttk.Entry(side_panel)
        self.artist_entry.pack(fill="x", pady=(4, 10))

        ttk.Label(side_panel, text="Duration (mm:ss)", style="Field.TLabel").pack(anchor="w")
        self.duration_entry = ttk.Entry(side_panel)
        self.duration_entry.insert(0, "03:30")
        self.duration_entry.pack(fill="x", pady=(4, 12))

        ttk.Button(
            side_panel,
            text="+  Add Track",
            command=self.add_track,
            style="Primary.TButton",
        ).pack(fill="x")

        ttk.Label(
            side_panel,
            text="Navigation wraps around the playlist in both directions.",
            style="Subtitle.TLabel",
            wraplength=270,
            justify="left",
        ).pack(anchor="w", pady=(15, 0))

        ttk.Separator(outer).pack(fill="x", pady=(0, 10))
        ttk.Label(outer, textvariable=self.status_var, style="Status.TLabel").pack(anchor="w")

    @staticmethod
    def format_duration(duration):
        minutes = duration // 60
        seconds = duration % 60
        return f"{minutes:02d}:{seconds:02d}"

    @staticmethod
    def parse_duration(value):
        parts = value.strip().split(":")
        if len(parts) != 2 or not parts[0].isdigit() or not parts[1].isdigit():
            raise ValueError("Enter the duration in mm:ss format, for example 03:45.")

        minutes = int(parts[0])
        seconds = int(parts[1])
        if seconds > 59:
            raise ValueError("Seconds must be between 00 and 59.")

        duration = minutes * 60 + seconds
        if duration <= 0:
            raise ValueError("Duration must be greater than zero.")
        return duration

    def add_track(self):
        title = self.title_entry.get().strip()
        artist = self.artist_entry.get().strip()
        duration_text = self.duration_entry.get().strip()

        if not title or not artist:
            messagebox.showwarning("Missing information", "Enter both a track title and an artist.")
            return

        try:
            duration = self.parse_duration(duration_text)
        except ValueError as error:
            messagebox.showwarning("Invalid duration", str(error))
            return

        self.playlist.append(title, artist, duration)
        self.title_entry.delete(0, tk.END)
        self.artist_entry.delete(0, tk.END)
        self.title_entry.focus_set()
        self.refresh_playlist()
        self.status_var.set(f"Added track: {title} — {artist}")

    def next_track(self):
        if self.playlist.is_empty():
            self.status_var.set("The playlist is empty. Add a track first.")
            return

        track = self.playlist.next_track()
        self.refresh_playlist()
        self.status_var.set(f"Current track: {track.title}")

    def previous_track(self):
        if self.playlist.is_empty():
            self.status_var.set("The playlist is empty. Add a track first.")
            return

        track = self.playlist.prev_track()
        self.refresh_playlist()
        self.status_var.set(f"Current track: {track.title}")

    def delete_current(self):
        deleted = self.playlist.delete_current()
        if deleted is None:
            self.status_var.set("There is no current track to delete.")
            return

        self.refresh_playlist()
        self.status_var.set(f"Deleted track: {deleted.title}")

    def select_track(self, event=None):
        selected = self.track_tree.selection()
        if not selected:
            return

        track = self.playlist.find_by_id(selected[0])
        if track is not None and self.playlist.set_current(track):
            self.refresh_playlist()
            self.status_var.set(f"Current track: {track.title}")

    def refresh_playlist(self):
        for item_id in self.track_tree.get_children():
            self.track_tree.delete(item_id)

        current = self.playlist.current
        for track in self.playlist.iter_nodes():
            tags = ("current",) if track is current else ()
            self.track_tree.insert(
                "",
                "end",
                iid=str(id(track)),
                values=(track.title, track.artist, self.format_duration(track.duration)),
                tags=tags,
            )

        total = self.playlist.count()
        self.count_label.configure(text=f"{total} TRACK" if total == 1 else f"{total} TRACKS")

        if current is None:
            self.current_title.configure(text="No track selected")
            self.current_artist.configure(text="Add a track to your playlist")
            self.current_duration.configure(text="--:--")
        else:
            self.current_title.configure(text=current.title)
            self.current_artist.configure(text=current.artist)
            self.current_duration.configure(text=self.format_duration(current.duration))


def main():
    root = tk.Tk()
    MusicPlayerApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
