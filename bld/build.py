import os
from datetime import datetime
import util

cfg: dict = util.loadCfg()
buildDir: str = f"{cfg["outDir"]}/{datetime.now().strftime("%H_%M_%S")}"
wasteDir: str = f"{buildDir}/waste"

def compile() -> bool:
    for src in cfg["sources"]:
        print(f"compiling '{src}.cxx'...")

        if not 0 == os.system(f"clang++ -c {src}.cxx -o {wasteDir}/{os.path.basename(src)}.o"):
            print(f"compilation of '{src}.cxx' failed")
            return False

    return True

def link() -> bool:
    print("linking sources...")

    srcs: str = ""
    for src in cfg["sources"]:
        srcs += f"{wasteDir}/{os.path.basename(src)}.o "

    return 0 == os.system(f"clang++ {srcs} -o {buildDir}/{cfg["binName"]}")

def build() -> str:
    util.setup()

    if not os.path.exists(cfg["outDir"]):
        os.makedirs(cfg["outDir"])

    os.makedirs(buildDir)
    os.makedirs(wasteDir)

    if not compile() or not link():
        os.rmdir(buildDir)
        print("build failed")
        return "null"

    print("build successful")
    return buildDir

if __name__ == "__main__": build()