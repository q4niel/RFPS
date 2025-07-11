import os
from datetime import datetime
import shutil
import util

cfg: dict = util.loadCfg()
buildDir: str = f"{cfg["outDir"]}/{datetime.now().strftime("%H_%M_%S")}"
wasteDir: str = f"{buildDir}/waste"

def compile() -> bool:
    includes: str = ""
    for include in cfg["includes"]:
        includes += f"-I{include} "

    for src in cfg["sources"]:
        print(f"compiling '{src}.cxx'...")

        if not 0 == os.system(f"clang++ {includes} -c {src}.cxx -o {wasteDir}/{os.path.basename(src)}.o"):
            print(f"compilation of '{src}.cxx' failed")
            return False

    return True

def link() -> bool:
    print("linking sources...")

    srcs: str = ""

    for src in cfg["sources"]:
        srcs += f"{wasteDir}/{os.path.basename(src)}.o "

    for lib in cfg["staticLibs"]:
        srcs += f"{lib}.a "

    return 0 == os.system(f"clang++ {srcs} -o {buildDir}/{cfg["binName"]}")

def build() -> str:
    util.setup()

    if not os.path.exists(cfg["outDir"]):
        os.makedirs(cfg["outDir"])

    os.makedirs(buildDir)
    os.makedirs(wasteDir)

    if not compile() or not link():
        shutil.rmtree(buildDir)
        print("build failed")
    else:
        print("build successful")

    return buildDir

if __name__ == "__main__": build()