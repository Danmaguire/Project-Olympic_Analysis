

def standardScatter(x,y,ytitle,xtitle,title):
    fig, ax = plt.subplots()
    ax.scatter(x,
                y,
                s=50,
                marker='o',
                facecolors='#DC143C', 
                edgecolors='#DC143C',
                )
    
    ax.set_ylabel(ytitle,fontsize=17)
    ax.set_xlabel(xtitle,fontsize=17)
    ax.set_title("\n"+title+"\n",fontsize=24)
    ax.locator_params(nbins=4)
    plt.tight_layout()
    plt.show()

def standardScatterWithRect(x,y,ytitle,xtitle,title,text,Rcorner,Rwidth,Rheight):
    fig, ax = plt.subplots()
    ax.scatter(x,
                y,
                s=50,
                marker='o',
                facecolors='#DC143C', 
                edgecolors='#DC143C',
                )
    ax.add_patch(
        patches.Rectangle(
            Rcorner,
            Rwidth,
            Rheight,
            fill=False
        )
    )
    ax.text(Rcorner[0]+Rwidth+.01, Rcorner[1]+(Rheight/2),text, color='Black', fontsize=15)
    
    ax.set_ylabel(ytitle,fontsize=17)
    ax.set_xlabel(xtitle,fontsize=17)
    ax.set_title("\n"+title+"\n",fontsize=24)
    ax.locator_params(nbins=4)
    plt.tight_layout()
    plt.show()

def standardScatterLine(x,y,ytitle,xtitle,title):
    x_nparray = (new_df['norm_Rating_Share'].values).reshape(len(x), 1)
    y_nparray = (new_df.norm_Population.values).reshape(len(y), 1)
    
    regr = LinearRegression()
    regr.fit(x_nparray, y_nparray)
    
    fig, ax = plt.subplots()
    
    ax.plot(x_nparray, regr.predict(x_nparray), color='k', linewidth=3)
    ax.scatter(x,
                y,
                marker='o',
                facecolors='#DC143C', 
                edgecolors='#DC143C',
                )
    
    ax.set_ylabel(ytitle,fontsize=17)
    ax.set_xlabel(xtitle,fontsize=17)
    ax.set_title("\n"+title+"\n",fontsize=24)
    ax.locator_params(nbins=4)
    plt.tight_layout()
    plt.show()