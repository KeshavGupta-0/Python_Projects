import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
# Prevents blank/crashing exe,Required for Tkinter + matplotlib apps
import matplotlib
matplotlib.use("TkAgg")

import shm
import damped_shm
import numpy as np

# root
root = tk.Tk()
root.title("Harmonic Motion Simulator")
root.geometry("1200x700")
root.configure(bg="#020617")


# animation state
animation_id = None
paused = False
current_index = 0

anim_data = {
    "ax": None,
    "canvas": None,
    "x": None,
    "ys": None,
    "lines": None
}

# stop animation
def stop_animation():
    global animation_id
    if animation_id is not None:
        root.after_cancel(animation_id)
        animation_id = None

# resume loop
def _resume_animation_loop():
    global animation_id, current_index

    def update():
        global current_index, animation_id

        if paused or current_index >= len(anim_data["x"]):
            return

        for line, y in zip(anim_data["lines"], anim_data["ys"]):
            line.set_data(
                anim_data["x"][:current_index],
                y[:current_index]
            )

        anim_data["canvas"].draw()
        current_index += 1
        animation_id = root.after(20, update)

    update()

# animate plot
def animate_plot(ax, canvas, x, y_list, colors, labels):
    global current_index, paused, anim_data

    stop_animation()
    paused = False
    current_index = 0

    ax.clear()
    ax.grid(alpha=0.3)
    ax.axhline(0, color="black", linewidth=2)

    ax.set_xlim(0, 2*np.pi)
    ax.set_xticks([0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi])
    ax.set_xticklabels(["0", "π/2", "π", "3π/2", "2π"])

    ymax = max(np.max(np.abs(y)) for y in y_list)
    if ymax == 0:
        ymax = 1
    ax.set_ylim(-1.1*ymax, 1.1*ymax)

    lines = []
    for y, c, lbl in zip(y_list, colors, labels):
        line, = ax.plot([], [], color=c, linewidth=2, label=lbl)
        lines.append(line)

    if len(labels) > 1:
        ax.legend()

    anim_data = {
        "ax": ax,
        "canvas": canvas,
        "x": x,
        "ys": y_list,
        "lines": lines
    }

    _resume_animation_loop()

# pause
def pause():
    global paused
    paused = True

# resume
def resume():
    global paused
    if paused:
        paused = False
        _resume_animation_loop()

# restart
def restart():
    global current_index, paused

    if anim_data["ax"] is None:
        return

    stop_animation()
    paused = False
    current_index = 0
    _resume_animation_loop()

# top bar
top = tk.Frame(root, bg="#020617", height=60)
top.pack(fill="x")

def show_shm():
    shm_frame.tkraise()

def show_damped():
    damped_frame.tkraise()

tk.Button(top, text="SHM", bg="#38bdf8", fg="black",
          font=("Segoe UI", 11, "bold"), command=show_shm
          ).pack(side="left", expand=True, fill="x", padx=5, pady=10)

tk.Button(top, text="Damped SHM", bg="#a855f7", fg="white",
          font=("Segoe UI", 11, "bold"), command=show_damped
          ).pack(side="left", expand=True, fill="x", padx=5, pady=10)

# container
container = tk.Frame(root, bg="#020617")
container.pack(fill="both", expand=True)

# plot helper
def create_plot_area(parent):
    fig = Figure(figsize=(6, 4), dpi=100)
    ax = fig.add_subplot(111)
    ax.grid()

    canvas = FigureCanvasTkAgg(fig, master=parent)
    canvas.get_tk_widget().pack(fill="both", expand=True)

    return fig, ax, canvas

# slider
def slider(parent, text, var, frm, to, step):
    tk.Label(parent, text=text, fg="white", bg="#020617").pack(anchor="w")

    scale = tk.Scale(
        parent,
        variable=var,
        from_=frm,
        to=to,
        resolution=step,
        orient="horizontal",
        bg="#020617",
        fg="white",
        highlightthickness=0
    )
    scale.pack(fill="x", pady=(0, 10))

    scale.bind("<Button-1>", lambda e: stop_animation())
    scale.bind("<B1-Motion>", lambda e: stop_animation())

# shm frame
shm_frame = tk.Frame(container, bg="#020617")
shm_controls = tk.Frame(shm_frame, bg="#020617", width=320)
shm_controls.pack(side="left", fill="y", padx=10, pady=10)
shm_controls.pack_propagate(False)

shm_plot = tk.Frame(shm_frame, bg="#020617")
shm_plot.pack(side="right", fill="both", expand=True)

fig_s, ax_s, canvas_s = create_plot_area(shm_plot)

A_s = tk.DoubleVar(value=2)
w_s = tk.DoubleVar(value=2)
phi_s = tk.DoubleVar(value=0)

slider(shm_controls, "Amplitude (A)", A_s, 0.5, 5, 0.1)
slider(shm_controls, "Angular Frequency (ω)", w_s, 0.5, 5, 0.1)
slider(shm_controls, "Phase (φ)", phi_s, 0, 360, 15)

# shm control buttons
shm_controls_bar = tk.Frame(shm_plot, bg="#020617")
shm_controls_bar.pack(side="bottom", pady=5)

tk.Button(shm_controls_bar, text="Pause", command=pause).pack(side="left", padx=5)
tk.Button(shm_controls_bar, text="Resume", command=resume).pack(side="left", padx=5)
tk.Button(shm_controls_bar, text="Restart", command=restart).pack(side="left", padx=5)

# shm plot
def plot_shm(func, label):
    model = shm.shm(A_s.get(), w_s.get(), phi_s.get())
    t = model.t
    y = func(model, t)

    animate_plot(
        ax_s, canvas_s, t,
        [y], ["#38bdf8"], [label]
    )

def plot_shm_energy_comp():
    model = shm.shm(A_s.get(), w_s.get(), phi_s.get())
    t = model.t

    animate_plot(
        ax_s, canvas_s, t,
        [model.ke(t), model.pe(t), model.te(t)],
        ["#0ea5e9", "#22c55e", "#facc15"],
        ["KE", "PE", "TE"]
    )

def shm_button(text, cmd):
    tk.Button(shm_controls, text=text, width=26, height=2,
              bg="#38bdf8", fg="black",
              font=("Segoe UI", 10, "bold"),
              command=cmd).pack(pady=4)

shm_button("Displacement", lambda: plot_shm(lambda m, t: m.x(t), "x(t)"))
shm_button("Velocity", lambda: plot_shm(lambda m, t: m.v(t), "v(t)"))
shm_button("Acceleration", lambda: plot_shm(lambda m, t: m.a(t), "a(t)"))
shm_button("Kinetic Energy", lambda: plot_shm(lambda m, t: m.ke(t), "KE"))
shm_button("Potential Energy", lambda: plot_shm(lambda m, t: m.pe(t), "PE"))
shm_button("Total Energy", lambda: plot_shm(lambda m, t: m.te(t), "TE"))
shm_button("Energy Comparison", plot_shm_energy_comp)

# damped shm frame
damped_frame = tk.Frame(container, bg="#020617")
damped_controls = tk.Frame(damped_frame, bg="#020617", width=320)
damped_controls.pack(side="left", fill="y", padx=10, pady=10)
damped_controls.pack_propagate(False)

damped_plot = tk.Frame(damped_frame, bg="#020617")
damped_plot.pack(side="right", fill="both", expand=True)

fig_d, ax_d, canvas_d = create_plot_area(damped_plot)

A_d = tk.DoubleVar(value=2)
w_d = tk.DoubleVar(value=2)
g_d = tk.DoubleVar(value=0.2)
phi_d = tk.DoubleVar(value=0)

slider(damped_controls, "Amplitude (A)", A_d, 0.5, 5, 0.1)
slider(damped_controls, "Angular Frequency (ω)", w_d, 0.5, 5, 0.1)
slider(damped_controls, "Damping (β)", g_d, 0.1, 2, 0.1)
slider(damped_controls, "Phase (φ)", phi_d, 0, 360, 15)

# damped control buttons
damped_controls_bar = tk.Frame(damped_plot, bg="#020617")
damped_controls_bar.pack(side="bottom", pady=5)

tk.Button(damped_controls_bar, text="Pause", command=pause).pack(side="left", padx=5)
tk.Button(damped_controls_bar, text="Resume", command=resume).pack(side="left", padx=5)
tk.Button(damped_controls_bar, text="Restart", command=restart).pack(side="left", padx=5)

# damped plot
def plot_damped(func, label):
    model = damped_shm.damped_shm(
        A_d.get(), w_d.get(), phi_d.get(), g_d.get()
    )
    t = model.t
    y = func(model, t)

    animate_plot(
        ax_d, canvas_d, t,
        [y], ["#a855f7"], [label]
    )

def plot_damped_energy_comp():
    model = damped_shm.damped_shm(
        A_d.get(), w_d.get(), phi_d.get(), g_d.get()
    )
    t = model.t

    animate_plot(
        ax_d, canvas_d, t,
        [model.ke(t), model.pe(t), model.te(t)],
        ["#60a5fa", "#4ade80", "#fde047"],
        ["KE (damped)", "PE (damped)", "TE (damped)"]
    )

def damped_button(text, cmd):
    tk.Button(damped_controls, text=text, width=26, height=2,
              bg="#a855f7", fg="white",
              font=("Segoe UI", 10, "bold"),
              command=cmd).pack(pady=4)

damped_button("Displacement", lambda: plot_damped(lambda m, t: m.x(t), "x(t)"))
damped_button("Velocity", lambda: plot_damped(lambda m, t: m.v(t), "v(t)"))
damped_button("Acceleration", lambda: plot_damped(lambda m, t: m.a(t), "a(t)"))
damped_button("Kinetic Energy", lambda: plot_damped(lambda m, t: m.ke(t), "KE"))
damped_button("Potential Energy", lambda: plot_damped(lambda m, t: m.pe(t), "PE"))
damped_button("Total Energy", lambda: plot_damped(lambda m, t: m.te(t), "TE"))
damped_button("Energy Comparison", plot_damped_energy_comp)

# overlap
for f in (shm_frame, damped_frame):
    f.place(x=0, y=0, relwidth=1, relheight=1)

shm_frame.tkraise()
root.mainloop()