import tkinter as tk
from tkinter import font
from PIL import Image, ImageTk
import time

# Initialize the main window
root = tk.Tk()
root.title("LF8 Full Gambit Overlay")
root.geometry("1920x1080")  # Full HD Resolution
root.configure(bg="black")

# Define custom fonts
team_font = font.Font(family="Arial", size=18, weight="bold")
score_font = font.Font(family="Arial", size=36, weight="bold")
timer_font = font.Font(family="Arial", size=48, weight="bold")
map_font = font.Font(family="Arial", size=24, weight="bold")

# Custom colors
primary_color = "#00FF00"  # Neon green, for VCT feel
secondary_color = "#FF0000"  # Red, for important highlights

# Agent images directory
AGENT_IMAGES_DIR = "images/agents/"

# Simplified mapping (ensure these paths exist)
agent_image_mapping = {
    'Jett': 'jett.png',
    'Phoenix': 'phoenix.png',
    'Sage': 'sage.png',
    # Add other agents and ensure these images exist in your directory
}

# Function to load images safely
def load_image(agent):
    try:
        image_path = AGENT_IMAGES_DIR + agent_image_mapping.get(agent, 'default.png')
        image = Image.open(image_path).resize((50, 50))
        return ImageTk.PhotoImage(image)
    except Exception as e:
        print(f"Error loading image for {agent}: {e}")
        return None

# Function to create player labels with agent images
def create_player_labels(frame, players):
    for player in players:
        agent = player['agent']
        stats = player['stats']

        player_frame = tk.Frame(frame, bg="black")
        player_frame.pack(anchor="w", padx=10, pady=2)

        # Load and display the agent image
        agent_photo = load_image(agent)
        if agent_photo:
            agent_image_label = tk.Label(player_frame, image=agent_photo, bg="black")
            agent_image_label.image = agent_photo  # Keep a reference to avoid garbage collection
            agent_image_label.pack(side="left")

        # Display player stats
        player_stats = tk.Label(player_frame, text=stats, font=team_font, fg="white", bg="black")
        player_stats.pack(side="left", padx=10)

# Top-Center: Score and Timer
score_label = tk.Label(root, text="9 - 7", font=score_font, fg=primary_color, bg="black")
score_label.place(relx=0.5, rely=0.05, anchor="center")

timer_label = tk.Label(root, text="1:38", font=timer_font, fg="white", bg="black")
timer_label.place(relx=0.5, rely=0.15, anchor="center")

spike_status_label = tk.Label(root, text="Spike: Not Planted", font=team_font, fg=secondary_color, bg="black")
spike_status_label.place(relx=0.5, rely=0.25, anchor="center")

# Top-Left: Map Information
map_label = tk.Label(root, text="Current: Lotus | Next: Haven, Bind", font=map_font, fg="white", bg="black")
map_label.place(relx=0.05, rely=0.05, anchor="nw")

# Lower Left: Attacking Team Information
attacking_team_frame = tk.Frame(root, bg="black", bd=2, highlightbackground="red", highlightthickness=2)
attacking_team_frame.place(relx=0.05, rely=0.6, relwidth=0.4, relheight=0.3)

# Lower Right: Defending Team Information
defending_team_frame = tk.Frame(root, bg="black", bd=2, highlightbackground="blue", highlightthickness=2)
defending_team_frame.place(relx=0.55, rely=0.6, relwidth=0.4, relheight=0.3)

# Dummy data (simplified for testing)
attacking_team_data = [
    {"agent": "Jett", "stats": "Player 1: 100 HP | 100 Armor | $3000"},
    {"agent": "Phoenix", "stats": "Player 2: 75 HP | 50 Armor | $2400"}
]

defending_team_data = [
    {"agent": "Sage", "stats": "Player 6: 100 HP | 100 Armor | $4000"},
    {"agent": "Jett", "stats": "Player 7: 80 HP | 0 Armor | $1200"}
]

# Create the player labels with agent images
create_player_labels(attacking_team_frame, attacking_team_data)
create_player_labels(defending_team_frame, defending_team_data)

# Function to update the timer
def update_timer():
    current_time = time.strftime("%M:%S")
    timer_label.config(text=current_time)
    root.after(1000, update_timer)  # Update every second

# Function to update the score
def update_score():
    score_label.config(text=f"9 - 7")
    root.after(10000, update_score)  # Update every 10 seconds (for demonstration)

# Start updating the GUI elements
update_timer()
update_score()

# Run the main loop
root.mainloop()