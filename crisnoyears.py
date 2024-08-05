"""
Created on 6/8/24
@author: helloamyzhang
"""
if __name__ == '__main__': # DON'T MESS WITH LINES 5-11
    # icb_codes and years come from ICB_list_postww2 in dropbox.
    icb_codes = "111  113  114  115  116  118  119  120  121  123  125  127  128  129  132  133  134  135  136  139  140  142  144  145  146  147  149  150  152  153  154  155  156  159  162  165  166  167  168  169  170  171  172  173  175  176  177  178  180  181  182  183  184  185  186  187  193  194  195  196  197  198  199  202  203  204  205  206  208  209  210  211  212  213  214  216  219  220  222  223  224  225  226  227  230  231  232  234  235  237  238  241  242  243  245  246  247  248  249  254  255  257  258  259  260  261  263  267  270  272  274  277  281  282  284  285  287  288  290  291  292  293  294  295  296  298  300  301  303  304  305  307  309  310  311  314  315  317  320  324  321  322  325  326  327  328  333  334  336  337  338  340  341  342  343  348  350  352  353  354  357  358  359  361  362  363  365  369  370  372  371  375  376  378  379  380  381  382  383  384  386  387  388  391  392  393  397  399  400  401  402  403  404  405  408  409  410  411  412  413  415  416  417  418  419  420  421  422  423  424  425  426  427  429  430  431  432  434  435  436  437  438  439  440  441  442  443  444  445  446  447  448  450  451  453  454  455  456  457  458  459  460  461  462  463  464  466  469  470  471  472  473  475  476  477  484  492  488  494  485  478  486  489  480  495  487  483  481  491  496  482  474      110  112  117  122  124  126  130  131  137  138  141  143  148  151  157  158  160  161  163  164  174  179  188  189  190  191  192  200  201  207  215  217  218  221  228  229  233  236  239  240  244  250  251  252  253  256  262  264  265  266  268  269  271  273  275  276  278  279  280  283  286  289  297  299  302  306  308  312  313  316  318  319  323  329  330  331  332  335  339  344  345  346  347  349  351  355  356  360  364  366  367  368  373  374  377  385  389  390  394  395  396  398  406  407  414  428  433  449  452  465  467  468  493  490  479"
    corresponding_icb_codes = icb_codes.split("  ")
    years = "08/07/1946  02/10/1947  02/21/1947  07/03/1947  07/21/1947  08/17/1947  10/24/1947  11/29/1947  02/13/1948  06/24/1948  09/23/1948  12/19/1948  12/25/1948  03/1949  06/25/1950  09/30/1950  02/12/1951  07/07/1951  07/30/1951  03/24/1953  04/16/1953  10/08/1953  12/12/1953  03/13/1954  08/1954  01/08/1955  02/28/1955  03/27/1955  07/26/1956  09/13/1956  10/15/1956  10/23/1956  02/26/1957  08/18/1957  02/01/1958  05/08/1958  07/17/1958  07/24/1958  11/27/1958  12/29/1958  04/25/1959  08/25/1959  11/28/1959  02/15/1960  06/24/1960  07/05/1960  08/20/1960  11/09/1960  03/09/1961  04/15/1961  05/19/1961  06/19/1961  07/17/1961  08/1961  09/18/1961  09/26/1961  05/06/1962  09/08/1962  09/26/1962  10/16/1962  02/11/1963  04/26/1963  10/01/1963  11/30/1963  12/11/1963  12/21/1963  12/21/1963  01/09/1964  02/07/1964  05/1964  07/30/1964  08/04/1964  12/03/1964  02/07/1965  04/08/1965  08/05/1965  10/14/1966  11/12/1966  05/17/1967  11/15/1967  01/21/1968  01/30/1968  03/18/1968  04/09/1968  02/22/1969  03/02/1969  03/08/1969  04/15/1969  06/15/1969  03/13/1970  09/15/1970  02/08/1971  03/25/1971  05/24/1971  10/20/1971  03/30/1972  09/17/1972  09/26/1972  10/23/1972  05/14/1973  10/05/1973  07/15/1974  12/14/1974  05/12/1975  07/12/1975  10/16/1975  11/23/1975  02/22/1976  06/27/1976  08/06/1976  08/17/1976  03/08/1977  07/14/1977  07/22/1977  09/24/1977  10/25/1977  12/05/1977  01/22/1978  04/15/1978  05/03/1978  05/11/1978  09/03/1978  09/10/1978  10/16/1978  10/30/1978  12/25/1978  02/12/1979  02/24/1979  03/1979  04/12/1979  06/01/1979  07/15/1979  11/04/1979  12/12/1979  01/27/1980  06/11/1980  08/14/1980  09/17/1980  12/05/1980  01/1981  01/06/1981  01/22/1981  04/04/1981  04/28/1981  04/28/1981  05/15/1981  10/28/1981  12/13/1981  03/31/1982  06/05/1982  06/30/1982  02/11/1983  04/18/1983  06/24/1983  10/19/1983  02/21/1984  03/16/1984  04/02/1984  06/05/1984  11/06/1984  11/19/1985  11/23/1985  12/20/1985  02/09/1986  02/10/1986  03/24/1986  05/19/1986  12/04/1986  12/12/1986  01/1987  01/05/1987  02/25/1987  03/01/1987  06/03/1987  07/31/1987  10/03/1987  11/03/1987  12/14/1987  03/06/1988  03/14/1988  12/21/1988  08/21/1989  08/30/1989  12/15/1989  01/14/1990  08/02/1990  06/25/1991  09/23/1991  10/06/1991  11/27/1991  01/1992  03/03/1992  03/12/1992  03/14/1992  03/1993  07/10/1993  12/1993  07/1994  10/07/1994  01/09/1995  05/22/1995  12/15/1995  01/26/1996  04/09/1996  08/31/1996  09/18/1996  10/08/1996  11/13/1997  01/24/1998  05/06/1998  05/11/1998  07/29/1998  08/07/1998  10/31/1998  02/20/1999  05/09/1999  09/04/1999  09/11/2001  12/13/2001  04/14/2002  05/16/2002  07/11/2002  07/27/2002  09/12/2002  10/04/2002  06/13/2003  10/04/2003  06/01/2004  06/10/2004  10/04/2005  12/18/2005  01/10/2006  05/05/2006  07/12/2006  03/31/2007  09/08/2007  12/26/2007  04/07/2008  07/08/2008  08/07/2008  03/11/2009  05/05/2009  03/26/2010  11/23/2010  02/04/2011  02/22/2011  05/19/2011  02/12/2013  08/21/2013  02/22/2014  05/02/2014  10/06/2014  08/2015  11/24/2015  01/06/2016  01/14/2017  01/20/2019  02/10/2018  02/14/2019  02/16/2017  04/01/2016  04/04/2017  04/07/2018  06/12/2016  06/18/2019  07/03/2017  08/07/1999  08/24/2016  09/06/2018  09/14/2019  09/18/2016        06/30/1946  11/13/1946  07/26/1947  02/22/1948  08/21/1948  12/11/1948  06/19/1949  08/19/1949  06/16/1952  02/08/1953  06/17/1953  10/14/1953  02/24/1955  08/10/1955  04/04/1957  05/31/1957  11/23/1957  12/01/1957  02/09/1958  02/21/1958  03/1960  12/26/1960  09/28/1961  10/30/1961  12/11/1961  03/29/1962  04/22/1962  11/01/1963  11/20/1963  01/19/1964  04/24/1965  10/09/1965  11/05/1965  03/23/1967  07/09/1968  12/28/1968  04/15/1969  10/22/1969  09/16/1970  11/22/1970  10/05/1971  01/19/1973  02/21/1973  03/20/1973  04/10/1973  11/18/1973  11/01/1975  11/28/1975  01/18/1976  02/15/1976  06/08/1976  06/09/1976  07/02/1976  08/09/1976  11/21/1976  12/20/1976  05/29/1977  06/25/1977  07/03/1977  08/31/1977  11/23/1977  03/14/1978  11/07/1978  01/28/1979  03/06/1979  06/01/1979  10/28/1979  03/01/1980  06/07/1980  08/20/1980  10/27/1980  11/25/1980  01/30/1981  07/30/1981  08/12/1981  08/23/1981  10/13/1981  03/22/1982  12/09/1982  11/02/1983  11/08/1983  11/20/1983  12/06/1983  03/08/1984  03/25/1984  06/14/1985  08/21/1985  12/20/1985  04/26/1986  08/19/1986  09/11/1986  09/23/1986  02/12/1987  02/15/1987  05/02/1987  04/18/1988  09/09/1989  10/07/1989  09/30/1990  03/23/1991  04/11/1991  08/28/1991  08/18/1992  09/25/1992  02/02/1995  10/01/1998  07/24/2001  04/12/2006  10/09/2006  04/03/2011  04/10/2012  10/03/2012  01/23/2019  04/15/2018  06/09/2016"
    corresponding_icb_years = [date[-4:] for date in years.split("  ")]
    # make sure years refers to TRIGGER DATE from the csv file in dropbox
    #print(corresponding_icb_years) # this line prints out the years

    """
    make sure years and icb_codes were copied and pasted correctly from 
    the file in dropbox/make sure they are the same length.
    """

    print(len(corresponding_icb_codes))
    print(len(corresponding_icb_years))
    print(len(corresponding_icb_years) == len(corresponding_icb_codes)) #
    # line 21's boolean must be True in order to proceed correctly

    """
    initializing a dictionary where the key = icb crisno code, value = year
    # of the crisis
    """

    my_dict = {}
    for i in range(len(corresponding_icb_codes)):
        my_dict[corresponding_icb_codes[i]] = corresponding_icb_years[i]


    """
    HERE: swap out want_years to a string of all the crisnos you want the 
    years of, separated by some delimitator. amy tip: copy and 
    paste the column of crisnos you want  years of from a csv file and paste 
    into your browser, then copy ALL of that string in your broswer and paste 
    it on the line you're initializing the variable (in this case, line 43).
    """

    # demarchi's cases crisno numbers. random cases that he was assigned that
    # we want the years of.
    want_years = "320 320 324 317 317 317 317 317 317 317 317 317 317 317 322 321 321 321 321 325 326 327 327 327 328 333 334 336 336 337 365 365 365 369 369 370 370 372 371 375 376 378 379 380 380 381 382 383 383 384 386 387 387 387"
    want_years_list = want_years.split(" ")

    for yr in want_years_list:
        print(my_dict[yr])

    # then, copy and paste the output from your terminal into your csv/excel
    # file where the crisnos from line 44 came from.





