import numpy as np


# Энтропияның есептесу функциясы
def entropy(y):
    # Бірден меткалардың бендерін алу және олардың санын анықтау
    _, counts = np.unique(y, return_counts=True)
    # Меткалардың верояттіліктерін есептеу
    probabilities = counts / len(y)
    # Формулаға сәйкес энтропияны есептеу
    return -np.sum(probabilities * np.log2(probabilities))


# Ақпараттың көмегінде жіберілген мәліметтердің кластары бойынша ақпараттың артқысыны есептеу функциясы
def information_gain(X, y, feature_index, threshold):
    # Ата-аналық ақпараттың энтропиясын есептеу
    parent_entropy = entropy(y)
    # Порогқа қарай ақпаратты бөлу
    left_indices = X[:, feature_index] <= threshold
    right_indices = X[:, feature_index] > threshold
    # Жиынымен бөлектерде біреулердің бар екендігін тексеру
    if np.sum(left_indices) == 0 or np.sum(right_indices) == 0:
        return 0
    # Сол және оң бөлектердің энтропияларын есептеу
    left_entropy = entropy(y[left_indices])
    right_entropy = entropy(y[right_indices])
    # Ақпаратты бөлетін бөлектердің энтропияларының ағымдалдырылған жиынын табу үшін
    child_entropy = (np.sum(left_indices) / len(y)) * left_entropy + (np.sum(right_indices) / len(y)) * right_entropy
    # Ағымдалдырылған ақпаратты есептеу
    return parent_entropy - child_entropy


# Ең көп рет кездесетін сыныптық белгілердің анықталуы үшін функция
def most_common_label(y):
    # Сыныптық белгілердің ең көп рет кездесуін анықтау
    return np.argmax(np.bincount(y))


# Көрсеткіш және порогқа бойынша ақпаратты бөлу функциясы
def split_dataset(X, y, feature_index, threshold):
    # Көрсеткіш және порогқа бойынша ақпаратты бөлу
    left_indices = X[:, feature_index] <= threshold
    right_indices = X[:, feature_index] > threshold
    # Бөлінген ақпаратты қайтару
    return X[left_indices], y[left_indices], X[right_indices], y[right_indices]


# Рекурсивті бағындау ақпаратты есептеу функциясы
def grow_tree(X, y, max_depth=None, depth=0):
    # Тоқталу шарты: максималды ұзындыға жеттік немесе барлық объекттер бір сыныпқа тиесілі
    if max_depth is not None and depth >= max_depth or len(np.unique(y)) == 1:
        return most_common_label(y)
    # Объекттердің саны мен көрсеткіштердің санын алу
    n_samples, n_features = X.shape
    # Ең жақсы ақпаратты бөлетін және оптимальды бөлу үшін ақпаратты іздеу
    best_gain = 0
    best_feature_index = None
    best_threshold = None
    for feature_index in range(n_features):
        thresholds = np.unique(X[:, feature_index])
        for threshold in thresholds:
            # Көрсеткіш және порогқа бойынша ақпаратты бөлу үшін ақпараттың артқысын есептеу
            gain = information_gain(X, y, feature_index, threshold)
            # Ең жақсы ақпаратты бөлетін және оптимальды бөлу үшін ақпаратты жаңарту
            if gain > best_gain:
                best_gain = gain
                best_feature_index = feature_index
                best_threshold = threshold
    # Егер ақпараттың артқысы 0 болса, ең көп рет кездесетін сыныптық белгілерді анықтау
    if best_gain == 0:
        return most_common_label(y)
    # Көрсеткіш және порогқа бойынша ақпаратты бөлу
    left_X, left_y, right_X, right_y = split_dataset(X, y, best_feature_index, best_threshold)
    # Сол жаңа және оң жаңа ақпаратты бағындау үшін рекурсивті функцияны шақыру
    left_tree = grow_tree(left_X, left_y, max_depth, depth + 1)
    right_tree = grow_tree(right_X, right_y, max_depth, depth + 1)
    # Оптимальды бөлумен ақпаратты қайтарады
    return (best_feature_index, best_threshold, left_tree, right_tree)


# Деректер ағашын құру функциясы
def create_decision_tree(X, y, max_depth=None):
    return grow_tree(X, y, max_depth)


# Деректер ағашы бойынша белгілерді есептеу функциясы
def predict_tree(x, tree):
    # Егер ағаш қолданушы болса, сыныптық белгіні көрсету
    if isinstance(tree, int):
        return tree
    # Қаралатын көрсеткіш, порог және оң/сол бағытын таңдау
    feature_index, threshold, left_tree, right_tree = tree
    if x[feature_index] <= threshold:
        return predict_tree(x, left_tree)
    else:
        return predict_tree(x, right_tree)


# Деректер ағашы бойынша белгілерді көрсету функциясы
def predict(X, tree):
    return np.array([predict_tree(x, tree) for x in X])


# Қолдану мисалы:

# Тесттеу үшін көрсеткіштердің мөлшері
X = np.array([[0, 0],
              [0, 1],
              [1, 0],
              [1, 1]])
# Тесттеу үшін сыныптар
y = np.array([0, 1, 1, 0])

# Деректер ағашын құру және оқу
tree = create_decision_tree(X, y, max_depth=2)

# Белгілерді көрсету
predictions = predict(X, tree)
print("Белгілер:", predictions)
