namespace TestingObserverLib
{
    public interface IMouse
    {
        public abstract void SetAliveStatus(MouseStatusInfo info);
        public abstract void SetPosition(MousePosInfo info);
        public static void Click(ClickEventInfo info) { }
    }

    public class Mouse : IMouse
    {
        private MouseStatusType _status = MouseStatusType.ALIVE;
        public MouseStatusType Status
        {
            set
            {
                SetAliveStatus(new MouseStatusInfo(value));
            }

            get => _status;
        }
        private double _x, _y;
        public double X
        {
            set
            {
                SetPosition(new MousePosInfo(value, _y));
            }
            get => _x;
        }
        public double Y
        {
            set
            {
                SetPosition(new MousePosInfo(_y, value));
            }
            get => _y;
        }

        public void SetAliveStatus(MouseStatusInfo info)
        {
            _status = info.Status;
            EventHolder<MouseStatusInfo>.Raise(info);
        }

        public void SetPosition(MousePosInfo info)
        {
            _x = info.X;
            _y = info.Y;
            EventHolder<MousePosInfo>.Raise(info);
        }

        public static void Click(ClickEventInfo info)
        {
            EventHolder<ClickEventInfo>.Raise(info);
        }
    }

    public enum ClickEventType
    {
        LEFT = 0,
        MIDDLE,
        RIGHT,
    }

    public class ClickEventInfo
    {
        public ClickEventType Type { get; }

        public ClickEventInfo(ClickEventType type)
        {
            Type = type;
        }
    }

    public enum MouseStatusType
    {
        ALIVE = 0,
        DEAD,
        SLEEP,
    }

    public class MouseStatusInfo
    {
        public MouseStatusType Status { get; }

        public MouseStatusInfo(MouseStatusType status)
        {
            Status = status;
        }
    }

    public class MousePosInfo
    {
        public double X, Y;

        public MousePosInfo(double x, double y)
        {
            X = x;
            Y = y;
        }
    }
}
