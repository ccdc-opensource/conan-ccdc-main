#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

from conans import ConanFile, CMake, tools
from conans.errors import ConanInvalidConfiguration

class CCDCMainConan(ConanFile):
    name = "ccdc-main"
    version = '2024.1.0'
    description = "Dependencies of main repository in CCDC"
    homepage = "https://ccdc.cam.ac.uk/"
    url = "https://github.com/conan-io/conan-center-index"
    topics = ("conan", "chemistry", "crystallography")
    license = "Proprietary"
    author = "Claudio Bantaloukas <cbantaloukas@ccdc.cam.ac.uk>"

    settings = "os", "arch", "compiler", "build_type"
    no_copy_source = True

    default_options = {"cpp-httplib:with_openssl": True}

    def build_requirements(self):
        if self.settings.os == 'Windows':
            self.build_requires("7zip/19.00")

        self.build_requires("cmake/3.28.1")
        self.build_requires("gtest/1.14.0")
        self.build_requires("ninja/1.11.1")
        self.build_requires("swig/4.1.0")

    def requirements(self):
        if self.settings.os != 'Windows':
            self.requires("fontconfig/2.14.2")

        self.requires("approvaltests.cpp/10.12.1")
        self.requires("ccdcboost/1.75.0")
        self.requires("ccdcsqlite3/3.17.0")
        self.requires("cpp-httplib/0.14.1")
        self.requires("cppad/20150000.9")
        self.requires("cryptopp/8.6.0")
        self.requires("csdprotobufs/1.0.666")
        self.requires("cqlprotobufs/1.0.136")
        self.requires("expat/2.6.0")
        self.requires("fasta/36.3.8f")
        self.requires("freetype/2.13.2")
        self.requires("gsoap/2.8.132")
        self.requires("inchi/1.06")
        self.requires("lexactivator/3.19.2")
        self.requires("lexfloatclient/4.7.2")
        self.requires("lexfloatserver/4.8.5")
        self.requires("libarchive/3.7.2")
        self.requires("libxl/3.8.2.0")
        self.requires("mariadb-connector-c/3.1.19")
        self.requires("openscenegraph/3.6.5")
        self.requires("openssl/3.0.13")
        self.requires("povray/3.7.0.8")
        self.requires("range-v3/0.11.0")
        self.requires("rapidjson/1.1.0")
        self.requires("rstatistics/2.11.1")
        self.requires("zlib/1.2.13")
        self.requires("zstd/1.5.5")
