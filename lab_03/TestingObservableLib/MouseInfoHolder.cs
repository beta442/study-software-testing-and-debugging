namespace TestingObserverLib
{
    public enum MouseScreenPosition
    {
        LEFT,
        RIGHT,
        TOP,
        DOWN,
    } 

    public class MouseInfoHolder
    {
        private Tuple<MouseScreenPosition, MouseScreenPosition> _screenPos = new(MouseScreenPosition.LEFT, MouseScreenPosition.TOP);
        private readonly List<ClickEventType> _mouseClicksHistory = new();
        private bool _keepCollectingInfo = true;
        public bool KeepCollectingInfo
        {
            get => _keepCollectingInfo;
            set
            {
                if (value != _keepCollectingInfo)
                {
                    SetTrackingStatus(value);
                }
            }
        }

        public MouseInfoHolder()
        {
            AttachListeners();

            EventHolder<MouseStatusInfo>.AddListener(OnMouseAliveStatusChange, true);
            KeepCollectingInfo = true;
        }

        ~MouseInfoHolder()
        {
            EventHolder<MouseStatusInfo>.RemoveListener(OnMouseAliveStatusChange);
            EventHolder<MousePosInfo>.RemoveListener(OnMousePosChange);
            EventHolder<ClickEventInfo>.RemoveListener(OnMouseClick);
        }

        public void SetTrackingStatus(bool keepTracking)
        {
            _keepCollectingInfo = keepTracking;
            if (!_keepCollectingInfo)
            {
                EventHolder<MousePosInfo>.RemoveListener(OnMousePosChange);
                EventHolder<ClickEventInfo>.RemoveListener(OnMouseClick);
            }
            else
            {
                AttachListeners();
            }
        }

        public Tuple<MouseScreenPosition, MouseScreenPosition> GetMousePosInfo()
        {
            return _screenPos;
        }

        public IEnumerable<ClickEventType> GetClickHistory()
        {
            return _mouseClicksHistory;
        }

        private void AttachListeners()
        {
            EventHolder<MousePosInfo>.AddListener(OnMousePosChange, false);
            EventHolder<ClickEventInfo>.AddListener(OnMouseClick, false);
        }

        private void OnMouseAliveStatusChange(MouseStatusInfo? info)
        {
            SetTrackingStatus(info!.Status.Equals(MouseStatusType.ALIVE));
        }

        private void OnMouseClick(ClickEventInfo? info)
        {
            _mouseClicksHistory.Add(info!.Type);
        }

        private void OnMousePosChange(MousePosInfo? info)
        {
            var vertical = (info!.Y > 500) ? MouseScreenPosition.DOWN : MouseScreenPosition.TOP;
            var horisontal = (info.X > 500) ? MouseScreenPosition.RIGHT : MouseScreenPosition.LEFT;

            _screenPos = new(horisontal, vertical);
        }
    }
}
