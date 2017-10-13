def pressureGauges(morning, evening):
    return [[min(morning[j], evening[j]) for j in range(len(morning))], [max(morning[k], evening[k]) for k in range(len(morning))]]
