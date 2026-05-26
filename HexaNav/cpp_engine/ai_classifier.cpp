#include "ai_classifier.h"

float AIClassifier::predictThreatScore(const std::string& url) {

    float score = 0.0f;

    if (url.find("crypto") != std::string::npos)
        score += 0.3f;

    if (url.find("free") != std::string::npos)
        score += 0.4f;

    if (url.find("login") != std::string::npos)
        score += 0.2f;

    return score;
}
