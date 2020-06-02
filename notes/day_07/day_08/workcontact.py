from work import Work


class WorkContact():
    ''' Contact class'''

    def __init__(self,
                work_name ='UNDEFINED',
                work_phone='UNDEFINED',
                work_address = Work()):
            
        if not isinstance(work_address, Work):
            print('[ERROR] work_address is not an Address class')
            return

        #Set class variables
        self.work_name = work_name
        self.work_phone = work_phone
        self.work_address = work_address

    def get(self):
        '''Return contact'''
        return {
            'work name': self.work_name,
            'work phone': self.work_phone,
            'work_address': self.work_address.get()
        }
        
