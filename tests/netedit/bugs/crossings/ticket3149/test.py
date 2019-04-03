#!/usr/bin/env python
# Eclipse SUMO, Simulation of Urban MObility; see https://eclipse.org/sumo
# Copyright (C) 2009-2019 German Aerospace Center (DLR) and others.
# This program and the accompanying materials
# are made available under the terms of the Eclipse Public License v2.0
# which accompanies this distribution, and is available at
# http://www.eclipse.org/legal/epl-v20.html
# SPDX-License-Identifier: EPL-2.0

# @file    test.py
# @author  Pablo Alvarez Lopez
# @date    2016-11-25
# @version $Id$

# import common functions for netedit tests
import os
import sys

testRoot = os.path.join(os.environ.get('SUMO_HOME', '.'), 'tests')
neteditTestRoot = os.path.join(
    os.environ.get('TEXTTEST_HOME', testRoot), 'netedit')
sys.path.append(neteditTestRoot)
import neteditTestFunctions as netedit  # noqa

# Open netedit
neteditProcess, referencePosition = netedit.setupAndStart(neteditTestRoot)

# Rebuild network
netedit.rebuildNetwork()

# go to inspect mode
netedit.inspectMode()

# select first left edge and change their junction
netedit.leftClick(referencePosition, 200, 260)
netedit.modifyAttribute(1, "B", False)
netedit.rebuildNetwork()

# select second left edge and change their junction
netedit.leftClick(referencePosition, 200, 320)
netedit.modifyAttribute(2, "A", False)
netedit.rebuildNetwork()

# select first right edge and change their junction
netedit.leftClick(referencePosition, 500, 260)
netedit.modifyAttribute(2, "B", False)
netedit.rebuildNetwork()

# select second right edge and change their junction
netedit.leftClick(referencePosition, 500, 320)
netedit.modifyAttribute(1, "A", False)
netedit.rebuildNetwork()

# Check undo redo
netedit.undo(referencePosition, 4)
netedit.rebuildNetwork()

# Check redo
netedit.redo(referencePosition, 4)
netedit.rebuildNetwork()

# save additionals
netedit.saveAdditionals()

# save network
netedit.saveNetwork()

# quit netedit
netedit.quit(neteditProcess)