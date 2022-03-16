'''
Created on 8 mars 2022

@author: slinux
'''
from wxRavenGUI.application.pluginsframework import *






'''

    This is a tentative of 2 side job with a transaction in between.
    ClientRequest is the client side
    ServerProcess is the server side
    
    
    


'''


#
#
# Client Side of the request
#
#
class Job_CreatePrivateWsTokenRemoteJob_ClientRequest(Job):
    '''
    classdocs
    '''

    
    def __init__(self, plugin, viewCallback=None, safeMode=True):
        '''
        Constructor
        '''
        
        Job.__init__(self, plugin.parentFrame, plugin, viewCallback, safeMode)
        
        self.jobName = f"New Private WS Token Request"
        self.jobId = f"{self.jobName} - {self.getNetworkName()}"
        
        
        self._txDialog = None
        self._jobTickTime = 10
        #self.setAllowRemoteExecution(val)
        #self.setReusable(False)
        #self.setExpiration(5)
        #self._initalJobRequest = ''
        #self.addExportParam('_initalJobRequest') 
        #self.setDelays(1, 0)
        #self.setNotification(False)
        self.addNetworkCompatibility('WS-RPC')
        self.setMaxRunningTime(600)
        #self.removeNetworkCompatibility('RPC')
        #self.addNetworkCompatibility('SQL')
        
        
    def JobProcess(self):
        
        #
        # 1 - Call WS and Request a Private Token
        #
        self.setProgress('Requesting new private token...')
        
        self.logger.info(f'{self.parentFrame.getNetworkType()}')
        if self.parentFrame.getNetworkType() != 'WS-RPC':
            self.setError("Active connexion must be a relay/webservice")
            return None
        
        
        #ravencoin = self.getNetworkRavencoin()
        
        network = self.getNetworkRPC()
        #network = self.parentFrame.getNetwork()
        _result = network.__RequestPrivateSessionToken__()
        
        if _result['error'] != None:
            self.setError(_result['error']['message'])
            return None
        
        #
        # 2 - Get the token and TX job to watch and parse.
        #
        _jobRemote = _result['result']['job']
        _privateToken = _result['result']['token']
        
        if _jobRemote != None and _privateToken != None:
            UserSystemNotification(self.parentFrame, "Token Requested !", "Token has been requested , TX Standby Job Received ", 'success')
            time.sleep(1)
        else:
            self.setError(_result['error']['message'])
            return None
        
        #
        #
        #time.sleep(1)
        
        
        
        
        
        
        _jobDatas = network.GetJob(_jobRemote)
        if _jobDatas['error'] != None:
            self.setError(_result['error']['message'])
            return None
        
        self.logger.info('Opening TX Dialog...')
        gplugin=self.parentFrame.GetPlugin('General')
        self.__MainThreadCall__(gplugin.OpenTxStandbyDialog, self,_jobDatas['result'] )
        
        #
        # 3 - Show the job with dialog and all tx infos
        #
        #Waiting funds in_adress
        _stopLoop = False
        while not _stopLoop:
            _jobDatas = network.GetJob(_jobRemote)
            
            
            self.logger.info(f'GetJob : {_jobDatas}')
            
            if _jobDatas['error'] != None:
                self.setError(_result['error']['message'])
                return None
            
            
            self.setProgress(_jobDatas['result']['_jobDetailedProgress'])
            if self._txDialog!=None:
                self._txDialog._Panel.__SetDatas__(_jobDatas['result'])
            else:
                self.logger.info('NO DIALOG TO REPORT TX DATAS')
            #self.__MainThreadCall__(self._txDialog.__SetDatas__, )
            
            if _jobDatas['result']['_jobPaymentStandby'] != None:
                #
                #Display payment infos
                
                pass
        
            if _jobDatas['result']['_jobDone'] == True:
                self.setResult("Transaction Recevied, Request Done.")
                _stopLoop = True
                 
                
            if not _stopLoop:    
                time.sleep(self._jobTickTime)
                
                
        if self._txDialog!=None:
            self._txDialog._Panel.__SetDatas__(_jobDatas['result'])        
        #
        # 3 - Confirm user
        #
        self.setResult(_privateToken)
        pass
    
    
    
    
    def SaveResult(self):
        gplugin=self.parentFrame.GetPlugin('General')
        gplugin.SetUserTokenSettingsAndEnableOption(self.getResult())
        _t = self.getResult()
        wx.CallAfter(UserAdvancedMessage, self.parentFrame, f'New Token {_t} Activated !', 'success',self.getResult() )
    
        
    
    



    
    

#
#
# Client Side of the request
#
#
class Job_CreatePrivateWsTokenRemoteJob_ServerProcess(Job):
    '''
    classdocs
    '''


    def __init__(self, plugin, viewCallback=None, safeMode=True):
        '''
        Constructor
        '''
        
        Job.__init__(self, plugin.parentFrame, plugin, viewCallback, safeMode)
        
        self.jobName = f"New Private WS Token Request (Server-Side)"
        self.jobId = f"{self.jobName} - {self.getNetworkName()}"
        
        self.setAllowRemoteExecution(False)
        self._inputToken = None
        self._watchTick = 20
        self.setReusable(False)
        #self.setExpiration(5)
        #self._initalJobRequest = ''
        #self.addExportParam('_initalJobRequest') 
        #self.setDelays(1, 0)
        #self.setNotification(False)
        #self.addNetworkCompatibility('WS-RPC')
        #self.addNetworkCompatibility('SQL')
        
        
    def JobProcess(self):
        
        
        #
        # Internal Job Safeguard to protect remote call despite options and settings
        #
        if self.__RemoteProtection__():
            return 
        
        
        #
        # 1 - Create a receive address and wait for funding
        #
        
        _JobTxUniqueIdentifier = f'New Private WS Token Request - {self._jobUniqueId}'
        ravencoin = self.getNetworkRavencoin()
        _jobAddress = ravencoin.JobsUtils.NewJobReceiveAddress(_JobTxUniqueIdentifier)
         
        self.setProgress(f"Waiting funds in {_jobAddress}")
        self.setPaymentStandby(_jobAddress, f"New Private WS Token Request - {self._inputToken}", PaymentAmount='1 RVN', PaymentTx=None, PaymentStatus='Waiting for TX...')        
        #
        # 2 - Detect funding and credit the token in the ws
        #
        
        _isfunded= False
        newsize = 0
        while _isfunded == False:
            
            #self.setProgress(f"Transaction found, session token update in progress !")
            _funded, _bal = ravencoin.JobsUtils.IsJobFunded(_JobTxUniqueIdentifier, 1.0,satoshis=False, assetName='RVN')
            self.logger.info(f'Checking job fund progress = {_funded} {_bal}')
            #
            # if funded, credits the token size to user
            #
            if _funded:
                #self.setResult("Transaction Recevied, Request Done.")
                #self.setProgress(f"Transaction found, session token update in progress !")
                self.setProgress(f"Transaction found, session token update in progress !")
                #self.setPaymentStandby(_jobAddress, f"New Private WS Token Request - {self._inputToken}", PaymentAmount='-', PaymentTx=None, PaymentStatus='Transaction DONE...')        
                self.setPaymentDone()
                wsplugin = self.parentFrame.GetPlugin('Webservices')
                _wsDaemon = wsplugin.GetWebserviceDaemonInstance()
                newsize= _wsDaemon.__CreditUserToken__(self._inputToken, rvn_amount=_bal, asset_amount=0.0)
                _isfunded=True
                break
            
            time.sleep(self._watchTick )    
        
        
        #
        # 3 - Confirm user
        #
        
        
        self.setProgress(f"The token {self._inputToken} has been credited with {newsize} !")
        self.setResult(f"The token {self._inputToken} has been credited with {newsize} !")
        #wipe adress
        #ravencoin.JobsUtils.IsJobFunded(self,_JobTxUniqueIdentifier, 1.0,satoshis=False, assetName='RVN')
    
    
    
    def SaveResult(self):
        pass