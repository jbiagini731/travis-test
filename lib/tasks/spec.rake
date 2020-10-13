# frozen_string_literal: true

require 'rake'
require 'rspec/core'
require 'rspec/core/rake_task'

namespace :spec do
  desc 'run all spec tests'
  RSpec::Core::RakeTask.new(:all) do |t|
    t.pattern = Dir.glob('spec/*_spec.rb')
    t.rspec_opts = '--format progress'
  end
end
