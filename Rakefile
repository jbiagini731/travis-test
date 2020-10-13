Dir.glob('lib/tasks/*.rake').each { |r| import r }

PROJECT_ROOT = __dir__.freeze
LIB_LOCATION = File.join(PROJECT_ROOT, 'lib')
$LOAD_PATH << LIB_LOCATION

task default: 'rubocop'
