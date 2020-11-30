class Rectangle:
    def __init__(self,width,height):
        self.height = height
        self.width=width
        
    def set_width(self,wd):
        self.width=wd
    
    def set_height(self,ht):
        self.height=ht
        
    def get_area(self):
        return self.width*self.height
    
    def get_perimeter(self):
        return (2*self.width + 2*self.height)
    
    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5
    
    def get_picture(self):
        if self.height>50 or self.width>50:
            return "Too big for picture."
        else:
            string=""
            for i in range(self.height):
                for j in range(self.width):
                    string+=("*")
                string+="\n"
            
            return string
        
    def __repr__(self):
        return self.__class__.__name__+"(width={}, height={})".format(self.width,self.height)
     
    def get_amount_inside(self,shape):
        area1=self.get_area()
        area2=shape.get_area()
        
        return int(area1/area2)
    
class Square(Rectangle):
    def __init__(self, sidelength):
        self.sidelength=sidelength    
        self.width=sidelength
        self.height=sidelength
        
    def set_side(self,sd):
        self.sidelength=sd
        self.width=sd
        self.height=sd

    def set_width(self,wd):
        self.set_side(wd)
    
    def set_height(self,ht):
        self.set_side(ht)
    
    def __repr__(self):
        return self.__class__.__name__+"(side={})".format(self.sidelength)
        
    
