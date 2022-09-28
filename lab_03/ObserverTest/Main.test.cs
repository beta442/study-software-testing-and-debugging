using Moq;
using TestingObserverLib;

namespace ObserverTest
{
    public class MouseInfoHolderTesting
    {
        [Fact]
        public void Clicking_history_is_collecting()
        {
            MouseInfoHolder holder = new();
            var excpectedHistory = new List<ClickEventType>() { ClickEventType.RIGHT, ClickEventType.LEFT };

            Mouse.Click(new ClickEventInfo(ClickEventType.RIGHT));
            Mouse.Click(new ClickEventInfo(ClickEventType.LEFT));

            Assert.Equal(holder.GetClickHistory(), excpectedHistory);
        }

        [Fact]
        public void Clicking_history_doesnt_collect_if_holder_is_turned_off()
        {
            MouseInfoHolder holder = new()
            {
                KeepCollectingInfo = false
            };

            Mouse.Click(new ClickEventInfo(ClickEventType.RIGHT));

            Assert.Empty(holder.GetClickHistory());
        }

        [Fact]
        public void Clicking_history_collecting_after_turning_on_golder()
        {
            MouseInfoHolder holder = new()
            {
                KeepCollectingInfo = false
            };
            holder.SetTrackingStatus(true);

            Mouse.Click(new ClickEventInfo(ClickEventType.RIGHT));

            Assert.NotEmpty(holder.GetClickHistory());
        }

        [Fact]
        public void Setting_mouse_por_changing_info_in_holder_1()
        {
            var mouse = new Mouse();
            var holder = new MouseInfoHolder();
            
            mouse.SetPosition(new MousePosInfo(300, 300));

            Assert.Equal(new Tuple<MouseScreenPosition, MouseScreenPosition>(MouseScreenPosition.LEFT, MouseScreenPosition.TOP), holder.GetMousePosInfo());
        }

        [Fact]
        public void Setting_mouse_por_changing_info_in_holder_2()
        {
            var mouse = new Mouse();
            var holder = new MouseInfoHolder();

            mouse.SetPosition(new MousePosInfo(501, 501));

            Assert.Equal(new Tuple<MouseScreenPosition, MouseScreenPosition>(MouseScreenPosition.RIGHT, MouseScreenPosition.DOWN), holder.GetMousePosInfo());
        }

        [Fact]
        public void Setting_mouse_off_turns_off_holder()
        {
            var mouse = new Mouse();
            var holder = new MouseInfoHolder();
            mouse.SetAliveStatus(new MouseStatusInfo(MouseStatusType.SLEEP));

            Mouse.Click(new ClickEventInfo(ClickEventType.LEFT));

            Assert.Empty(holder.GetClickHistory());
        }

        [Fact]
        public void Setting_mouse_pos
    }
}