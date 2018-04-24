def mergingVines(vines, n):
    def nTimes(n):
        def do_this_thang(func):
            def this_many_times(vines):
                for m in range(n):
                    vines = func(vines)

                return vines
            return this_many_times
        return do_this_thang

    @nTimes(n)
    def sumOnce(vines):
        res = [vines[i] + vines[i + 1] for i in range(0, len(vines) - 1, 2)]
        if len(vines) % 2 == 1:
            res.append(vines[-1])
        return res

    return sumOnce(vines)
