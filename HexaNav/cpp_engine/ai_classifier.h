#ifndef AI_CLASSIFIER_H
#define AI_CLASSIFIER_H

#include <string>

class AIClassifier {
public:
    float predictThreatScore(const std::string& url);
};

#endif
