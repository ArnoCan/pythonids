# -*- coding: utf-8 -*-
# The license for the configuration files 'conf.py' - only is MIT
#  
# Copyright 2019 Arno-Can Uestuensoez @Ingenieurbuero Arno-Can Uestuensoez
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software
# and associated documentation files (the "Software"), to deal in the Software without restriction,
# including without limitation the rights to use, copy, modify, merge, publish, distribute,
# sublicense, and/or sell copies of the Software, and to permit persons to whom the Software
# is furnished to do so, subject to the following conditions:
# 
#     The above copyright notice and this permission notice shall be included in all
#     copies or substantial portions of the Software.
# 
#     THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED,
#     INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A
#     PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
#     HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
#     OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
#     SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#
#
"""Custom configuration of *conf.py*.
to be appended to the file:
    ::

        ${BUILDDIR}/sphinx/apidoc/conf.py

"""

import sys
import os
import sphinx

from distutils.version import LooseVersion


__author__ = 'Arno-Can Uestuensoez'
__license__ = "Artistic-License-2.0 + Forced-Fairplay-Constraints"
__copyright__ = "Copyright (C) 2015-2019 Arno-Can Uestuensoez" \
                " @Ingenieurbuero Arno-Can Uestuensoez"
__version__ = '0.1.37'
__uuid__ = "45167c30-3261-4a38-9de4-d7151348ba48"

__docformat__ = "restructuredtext en"


#
# global metadata
#
project = 'setupdocx'
copyright = __copyright__
license = __license__
version = __version__
uuid = __uuid__


#
# add path for temporary tools required for this configuration
#
sys.path.insert(0, os.path.abspath(os.path.dirname(os.getcwd())))
sys.path.insert(0, os.path.abspath(os.getcwd()))



#
# required minimal sphinx version
#
# needs_sphinx = '1.0'


#
# running on read-the-docs
#
on_rtd = os.environ.get('READTHEDOCS', None) == 'True'


#
# required extensions
#
extensions = []
if on_rtd:
    extensions.extend(  # @UndefinedVariable
        [
            'sphinx.ext.mathjax.',
        ]
    )  #: provided by present conf.py @UndefinedVariable
elif LooseVersion(sphinx.__version__) < LooseVersion('1.4'):
    extensions.extend(  # @UndefinedVariable
        [
            'sphinx.ext.pngmath.',
        ]
    )  #: provided by present conf.py @UndefinedVariable
# else:
#     extensions.extend(  # @UndefinedVariable
#         [
#             'sphinx.ext.imgmath.',
#         ]
#     )  #: provided by present conf.py @UndefinedVariable

extensions.extend(  # @UndefinedVariable
    [
#        'javasphinx',
#         'matplotlib.sphinxext.only_directives',
#         'matplotlib.sphinxext.plot_directive',
        'sphinx.ext.autodoc',
        'sphinx.ext.doctest',
        'sphinx.ext.githubpages',
        'sphinx.ext.inheritance_diagram',
        'sphinx.ext.todo',
    ]
)  #: provided by present conf.py @UndefinedVariable

extensions.extend(  # @UndefinedVariable
    [
        'setupdocx.sphinx.ext.imagewrap',
        'setupdocx.sphinx.ext.literalincludewrap',
    ]
)  #: provided by setupdocx



#
# master document of toctree
#
master_doc = 'index'

#
# source_suffix = ['.rst', '.md']
#
source_suffix = '.rst'

#
# language for generated text by sphinx
#
# language = None

#
# patterns to ignore - relative to source directory
# (affects also html_static_path and html_extra_path)
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# style for syntax highlighting
pygments_style = 'sphinx'


###############################
#                             #
#        *** html ***         #
#                             #
###############################


#
# theme name
#
html_theme = 'alabaster'


#
# logo and favicon
#
html_logo = "_static/logo.png"
html_favicon = "_static/favicon.ico"  # 64x64 - 4bit/16    


#
# search paths - relative to the build directory + target directory
#
html_static_path = ['_static']
html_theme_path = ['_themes']
html_tepmplate_path = ['_templates']


#
# custom sidebar templates
#


#
# The default sidebars (for documents that don't match any pattern) are
# defined by theme itself.  Builtin themes are using these templates by
#
#   html_sidebars = {
#      default: ``['localtoc.html', 'relations.html', 'sourcelink.html', 'searchbox.html']``
#   }
#
# html_sidebars = {}


#
# html options
#
html_theme_options = {
    #  'logo': 'logo.png',
    # 
    'github_user': 'ArnoCan',
    # 
    'github_repo': 'setupdocx',
    # body_text_align
    # canonical_url
    # description
    # description_font_style
    # fixed_sidebar
    # logo
    # logo_name
    # logo_text_align
    # 
    'page_width': 800,
    # 'sidebar_width': 200,
    # touch_icon
    
    # Service links and badges
    #------------------------
    # analytics_id
    # badge_branch
    # codecov_button
    # donate_url
    # github_banner
    # 'github_button': True,
    # 'github_repo': "http://github.com/repo/",
    # github_user
    # gittip_user
    # tidelift_url
    # travis_button
    
    
    # Non-service sidebar control
    # ---------------------------
    # extra_nav_links
    # show_related
    # 'sidebar_collapse': True,
    # sidebar_includehidden
    
    # Header/footer options
    # ---------------------
    # show_powered_by
    # show_relbars
    
    # Style colors
    # ------------
    # anchor
    # anchor_hover_bg
    # anchor_hover_fg
    # body_text
    # code_highlight
    # footer_text
    # footnote_bg
    # footnote_border
    # gray_1
    # gray_2
    # gray_3
    # link_hover
    # link
    # narrow_sidebar_bg
    # narrow_sidebar_fg
    # narrow_sidebar_link
    # note_bg
    # note_border
    # pink_1
    # pink_2
    # pre_bg
    # relbar_border
    # seealso_bg
    # seealso_border
    # sidebar_header
    # sidebar_hr
    # sidebar_link
    # sidebar_list
    # sidebar_link_underscore
    # sidebar_search_button
    # sidebar_text
    # warn_bg
    # warn_border
    
    
    # Fonts
    # -----
    # caption_font_size
    # caption_font_family
    # code_font_size
    # code_font_family
    # font_family
    # font_size
    # head_font_family

}


def setup(app):
    app.add_stylesheet('custom.css')
    
    try:
        if os.environ.get('DOCX_APIREF') == '1':
            # create API reference, activates 'quick navigation' menu entry
            app.add_config_value('apiref', '1', True)
        
        else:
            app.add_config_value('apiref', '0', True)
    except:
        pass

