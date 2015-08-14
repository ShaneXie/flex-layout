from subprocess import call
import os

BUILDER_PATH = os.path.dirname(os.path.abspath(__file__))
ROOT_PATH = os.path.join(BUILDER_PATH, '..')
CSS_FOLDER_PATH = os.path.join(ROOT_PATH, 'css')
SCSS_FOLDER_PATH = os.path.join(ROOT_PATH, 'scss')


def scss_to_css():
  print "Generate CSS From SCSS"

  scss_file_path = os.path.join(SCSS_FOLDER_PATH, 'flex-layout.scss')
  css_file_path = os.path.join(CSS_FOLDER_PATH, 'flex-layout.css')
  css_min_file_path = os.path.join(CSS_FOLDER_PATH, 'flex-layout.min.css')

  cmd = "sass %s %s --style compact" % (scss_file_path, css_file_path)
  call(cmd, shell=True)

  print "Generate Minified CSS From SCSS"
  cmd = "sass %s %s --style compressed" % (scss_file_path, css_min_file_path)
  call(cmd, shell=True)

scss_to_css()