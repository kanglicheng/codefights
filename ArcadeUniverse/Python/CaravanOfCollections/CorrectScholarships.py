def correctScholarships(bestStudents, scholarships, allStudents):
    return (set(bestStudents) < set(scholarships) or set(bestStudents) == set(scholarships)) and set(scholarships) < set(allStudents)
