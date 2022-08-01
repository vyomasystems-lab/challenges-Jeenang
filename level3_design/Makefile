# See LICENSE.vyoma for details

TOPLEVEL_LANG ?= verilog

PWD=$(shell pwd)

VERILOG_SOURCES = $(PWD)/snoopy_cache.v               # provide your design path

TOPLEVEL :=   snoopy_cache        # design file
MODULE   :=     test_snoopy_cache# test file

include $(shell cocotb-config --makefiles)/Makefile.sim

#clean_all: clean
#	rm -rf *.xml sim_build __pycache__ 
