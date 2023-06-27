function tot = hnodd(n)
    % output the nth harmonic sum
    tot = 0;
    for i = 1:2:n
        tot = tot + 1/i;
    end
end
