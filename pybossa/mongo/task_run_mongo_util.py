from pybossa.mongo.base_mongo_util import BaseMongoUtil

class TaskRunMongoUtil(BaseMongoUtil):
    def __init__(self):
        super(TaskRunMongoUtil, self).__init__('taskruns')


    def consolidate_redundancy(self):
        ''' Go through redundant task run submissions and merge them into single documents
        '''
        pass