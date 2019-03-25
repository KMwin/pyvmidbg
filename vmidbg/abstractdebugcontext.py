from abc import ABC, abstractmethod


class AbstractDebugContext(ABC):

    def __init__(self, vmi):
        self.vmi = vmi
        # default thread: all threads
        self.cur_tid = -1

    @abstractmethod
    def attach(self):
        pass

    @abstractmethod
    def detach(self):
        pass

    @abstractmethod
    def get_dtb(self):
        pass

    @abstractmethod
    def dtb_to_desc(self, dtb):
        pass

    @abstractmethod
    def get_access_context(self, address):
        pass

    @abstractmethod
    def get_current_running_thread(self):
        pass

    @abstractmethod
    def get_thread(self, tid=None):
        pass

    @abstractmethod
    def list_threads(self):
        pass
