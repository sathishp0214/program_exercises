Kpi_report={}

class Access_point_base(object):
    def __init__(self):
        self.clientcount='clientcountformula'
        self.throughput='throughputformula'

    # def base_kpi_generation(self):
    #     return self.clientcount,self.throughput

class Access_point_V1(Access_point_base):
    def __init__(self):
        self.noisefloor='noisefloorv1_formula'
        self.cpuutilization='cpuutilizationv1_formula'
        Access_point_base.__init__(self)  #should pass it to super_class(with or without arguments), then only super_class attributes we can use

    def v1_generation(self):
        return self.noisefloor,self.cpuutilization



    # def ffff(self):
    #     print ('hi')
    #     print (self.d)

class Access_point_V1_derived(Access_point_V1):   #multi-level inheritance
    def __init__(self):
        self.txpower='txpowerformula'
        # Access_point_V1.__init__(self)
        super().__init__()  #use of super()




class Access_point_v2(Access_point_base):   #hierchical inheritance
    def __init__(self):
        self.noisefloor='noisefloorv2_formula'
        self.cpuutilization='cpuutilizationv2_formula'
        Access_point_base.__init__(self)

    def v2_generation(self):
        return self.noisefloor,self.cpuutilization


class Devices(object):    #composition class
    def __init__(self,devices):
        self.devices=devices

    def kpi_generate(self):
        for i in self.devices:
            # print('-' * 20, i, '-' * 20)
            if i[0]=='3' and i[1]=='7':
                obj=Access_point_V1()
                b,c=obj.v1_generation()
                a= [obj.clientcount,obj.throughput,b,c]
                Kpi_report[i]=a
                # print (obj.base_kpi_generation())
                print ()
            elif i[0] == '3' and i[1] == '8':
                obj = Access_point_v2()
                b, c = obj.v2_generation()
                a = [obj.clientcount, obj.throughput, b, c]
                Kpi_report[i] = a
            else:
                print ("invalid device type--",i)




obj=Devices(['3721','3820','3800','3700','67899'])
obj.kpi_generate()
print(Kpi_report)
print ("----",vars(obj))

obj1=Access_point_V1_derived()
print(obj1.txpower,obj1.noisefloor,obj1.clientcount)
# print (Access_point_V1.__mro__)
# print (vars(obj1))
# print (obj1.__dict__)
# print (vars(Access_point_V1_derived))
# print (Access_point_V1_derived.__dict__)

# ob=Access_point_V1()
# # print (ob.v1_generation())
# print (ob.ffff())