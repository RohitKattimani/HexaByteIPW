#include "sandbox_engine.h"
#include <iostream>

void SandboxEngine::isolateTab(int tabId) {
    std::cout << "Tab " << tabId << " isolated." << std::endl;
}

void SandboxEngine::releaseTab(int tabId) {
    std::cout << "Tab " << tabId << " released from sandbox." << std::endl;
}
