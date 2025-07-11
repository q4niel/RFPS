from build import build
import os
import util
import shutil

if __name__ == "__main__":
    buildDir: str = build()

    if os.path.exists(buildDir):
        print("\n- Running -\n")

        os.system(f"./{buildDir}/{util.loadCfg()["binName"]}")
        shutil.rmtree(buildDir)