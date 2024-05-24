import subprocess

def lazygit(commit_message):
    try:
        # Add all changes
        subprocess.run(["git", "add", "."], check=True)
        # Commit with the provided message
        subprocess.run(["git", "commit", "-a", "-m", commit_message], check=True)
        # Push the changes
        subprocess.run(["git", "push"], check=True)
        print("Changes have been successfully pushed.")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while running git command: {e}")

# Example usage:
commit_message = "i add it p17"
lazygit(commit_message)
