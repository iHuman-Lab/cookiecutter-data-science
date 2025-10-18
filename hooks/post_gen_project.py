import os
import shutil
import subprocess


def main():
    git_hooks_dir = os.path.join(".git", "hooks")
    githooks_src_dir = os.path.join(".githooks")

    if not os.path.isdir(git_hooks_dir):
        print("Warning: .git/hooks directory not found. Are you inside a git repo?")
        return

    # Copy pre-commit and pre-push hooks
    for hook in ["pre-commit", "pre-push"]:
        src = os.path.join(githooks_src_dir, hook)
        dst = os.path.join(git_hooks_dir, hook)

        if os.path.exists(src):
            shutil.copy(src, dst)
            os.chmod(dst, 0o755)
            print(f"Copied {hook} hook to .git/hooks")
        else:
            print(f"Hook {hook} not found in .githooks")

    # Install pre-commit package and hooks
    try:
        subprocess.run(["pip", "install", "--upgrade", "pre-commit"], check=True)
        subprocess.run(["pre-commit", "install", "--install-hooks"], check=True)
        print("pre-commit installed and hooks configured.")
    except Exception as e:
        print(f"Failed to install pre-commit or hooks: {e}")


if __name__ == "__main__":
    main()
