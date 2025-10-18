import os
import shutil
import subprocess


def main():
    if not os.path.exists(".git"):
        print("🔧 Initializing Git repository...")
        subprocess.run(["git", "init", "--initial-branch=main"], check=True)

    git_hooks_dir = os.path.join(".git", "hooks")
    githooks_src_dir = ".githooks"

    for hook in ["pre-commit", "pre-push"]:
        src = os.path.join(githooks_src_dir, hook)
        dst = os.path.join(git_hooks_dir, hook)

        if os.path.exists(src):
            shutil.copy(src, dst)
            os.chmod(dst, 0o755)
            print(f"✅ Copied {hook} to .git/hooks")
        else:
            print(f"⚠️  {hook} not found in .githooks")

    try:
        subprocess.run(["pip", "install", "--upgrade", "pre-commit"], check=True)
        subprocess.run(["pre-commit", "install", "--install-hooks"], check=True)
        print("✅ pre-commit installed and hooks configured.")
    except Exception as e:
        print(f"❌ Failed to install pre-commit or hooks: {e}")


if __name__ == "__main__":
    main()
