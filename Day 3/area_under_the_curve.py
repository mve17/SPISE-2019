def get_x_points(lower_bound,upper_bound,step_size): #helper function
    x_points=[]
    current_point=lower_bound
    while current_point<=upper_bound:
        x_points.append(current_point)
        current_point+=step_size
    return x_points

def area_under_parabola(): #part 1, the exact answer is 83.3333333
    x_points=get_x_points(-5,5,.1)
    #compute_area_estimate
    area=0
    for point_index in range(len(x_points)-1):
        point=x_points[point_index]
        next_point=x_points[point_index+1]
        middle_value=(.5*(point+next_point))**2
        area+=middle_value*.1
    return area

def area_under_parabola_variable(lower_bound,upper_bound,step_size): #part 2
    number_of_steps=(upper_bound-lower_bound)/step_size
    if number_of_steps==int(number_of_steps): #whole number of steps
        x_points=get_x_points(lower_bound,upper_bound,step_size)
        area=0
        for point_index in range(len(x_points)-1):
            point=x_points[point_index]
            next_point=x_points[point_index+1]
            middle_value=(.5*(point+next_point))**2
            area+=middle_value*step_size
        return area
    else:
        print('step size does not evenly divide range')

def area_under_function(function,lower_bound,upper_bound,step_size): #part 3
    number_of_steps=(upper_bound-lower_bound)/step_size
    if number_of_steps==int(number_of_steps): #whole number of steps
        x_points=get_x_points(lower_bound,upper_bound,step_size)
        area=0
        for point_index in range(len(x_points)-1):
            point=x_points[point_index]
            next_point=x_points[point_index+1]
            middle_value=function(.5*(point+next_point))
            area+=middle_value*step_size
        return area
    else:
        print('step size does not evenly divide range')

def parabola(x):
    return x**2

def area_simpsons_method(function,lower_bound,upper_bound,step_size): #part 4
    #check number of steps is an even integer
    number_of_steps=(upper_bound-lower_bound)/step_size
    if not (int(number_of_steps)==number_of_steps and int(number_of_steps)%2==0):
        print('step size does not evenly divide range')
    else:
        x_points=get_x_points(lower_bound,upper_bound,step_size)
        running_total=0
        for index in range(len(x_points)):
            if index==0 or index==len(x_points)-1:
                running_total+=function(x_points[index])
            elif index%2==1:
                running_total+=4*function(x_points[index])
            else:
                running_total+=2*function(x_points[index])
        return running_total*step_size/3

print(area_simpsons_method(parabola,-5,5,.1))


    
