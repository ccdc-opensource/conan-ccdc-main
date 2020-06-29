from conans import ConanFile, CMake, tools
from conans.errors import ConanInvalidConfiguration
import os


class CcdcMainConan(ConanFile):
    name = "ccdcmain"
    # version = '1.0.0'
    description = "Dependencies of main repository in CCDC"
    homepage = "https://ccdc.cam.ac.uk/"
    url = "https://github.com/conan-io/conan-center-index"
    topics = ("conan", "chemistry", "crystallography")
    license = "Proprietary"
    generators = "cmake_multi"

    settings = "os", "arch", "compiler", "build_type"
            
    def build_requirements(self):
        self.build_requires("zlib/1.2.11")
        self.build_requires("rapidjson/1.1.0")
        self.build_requires("cmake/3.17.3")
        self.build_requires("ninja/1.10.0")
        self.build_requires("ccdcsqlite3/3.17.0")
        self.build_requires("gtest/1.8.1")
        self.build_requires("openssl/1.1.1g")
        self.build_requires("protobuf/3.11.4")
        self.build_requires("gsoap/2.8.103")
        self.build_requires("freetype/2.10.1")
        self.build_requires("openscenegraph/3.6.3")
        self.build_requires("cppad/20150000.9")
        self.build_requires("fasta/36.3.8f")
        self.build_requires("lexactivator/3.9.2")
        self.build_requires("lexfloatclient/4.3.5")
        self.build_requires("lexfloatserver/4.3.1")
        self.build_requires("libxl/3.8.2.0")
        self.build_requires("povray/3.7.0.8")
        self.build_requires("installbuilder/20.4.0")
        self.build_requires("rstatistics/2.11.1")
        self.build_requires("swig/4.0.1")
        self.build_requires("inchi/1.04")