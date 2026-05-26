#ifndef SANDBOX_ENGINE_H
#define SANDBOX_ENGINE_H

class SandboxEngine {
public:
    void isolateTab(int tabId);
    void releaseTab(int tabId);
};

#endif
