namespace TestingObserverLib
{
    public class EventHolder<T> where T : class
    {
        private static readonly List<Action<T?>> _listeners = new();

        private static T? _currentInfoState;

        public static void AddListener(Action<T?> listener, bool instantNotify)
        {
            _listeners.Add(listener);
            if (instantNotify)
            {
                if (_currentInfoState != null)
                {
                    listener.Invoke(_currentInfoState);
                }
            }
        }

        public static void Raise(T? newState)
        {
            _currentInfoState = newState;
            foreach (var listener in _listeners)
            {
                listener.Invoke(newState);
            }
        }

        public static void RemoveListener(Action<T?> listener)
        {
            if (_listeners.Contains(listener))
            {
                _listeners.Remove(listener);
            }
        }
    }
}
