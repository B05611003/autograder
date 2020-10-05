require "AssessmentBase.rb"

module Hw0
  include AssessmentBase

  def assessmentInitialize(course)
    super("hw0",course)
    @problems = []
  end

end
