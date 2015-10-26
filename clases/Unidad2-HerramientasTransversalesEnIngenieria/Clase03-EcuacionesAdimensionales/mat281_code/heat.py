from matplotlib import pyplot as plt
import numpy as np

def html_table(list_of_lists):
    """
    Overridden list class which takes a 2-dimensional list of
    the form [[1,2,3],[4,5,6]], and renders an HTML Table in
    IPython Notebook.
    Taken from: http://calebmadrigal.com/display-list-as-table-in-ipython-notebook/
    """
    html = ["<table>"]
    for row in list_of_lists:
        html.append("<tr>")
        for col in row:
            html.append("<td>{0}</td>".format(col))
        html.append("</tr>")
    html.append("</table>")
    return ''.join(html)

# Solving the dimenstionless heat equation in an infinite rod.
def heat_equation(alpha, beta, N=100):
    x_array = np.linspace(0,1,N)
    t = 0.0
    tau_old = np.ones(N)
    tau_new = np.ones(N)
    tau_old[0] = alpha
    dx = x_array[1]-x_array[0]
    dt = 0.25*dx**2 # Stability
    c = dt/dx**2
    #temp = []
    while abs(1.-tau_old[-1])<abs(1.-beta):
        t += dt
        tau_new[ 0] = alpha
        tau_new[1:-1] = tau_old[1:-1] + c * (tau_old[:-2]-2*tau_old[1:-1]+tau_old[2:])
        tau_new[-1] = tau_old[-1] + c * (2*tau_old[-2]-5*tau_old[-3]+4*tau_old[-4]-1*tau_old[-5])
        tau_old = tau_new
	#temp.append(tau_old[-3])
    #plt.plot(temp)
    return t

def run():
    # Example
	
    alpha_min = 273./373.
    alpha_max = 373./273.
    alpha_array = np.linspace(alpha_min, alpha_max, 10)
    data = [[r'$\tau_b / \tau_a$ [1]',r'$\hat{t}^*$ [1]' ], ]
    for alpha in alpha_array:
        beta = 0.50 + 0.50*alpha
        #beta = 0.10 + 0.90*alpha
        t = heat_equation(alpha, beta)
        data.append([alpha, t])
    #plt.show()
    return html_table(data)

if __name__=="__main__":
    print run()
