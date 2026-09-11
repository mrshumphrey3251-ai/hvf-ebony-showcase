import 'package:flutter/material.dart';

class TelemetryFeedPanel extends StatelessWidget {
  const TelemetryFeedPanel({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    // [INTERNAL WEBSOCKET POLLING LOGIC REDACTED FOR PUBLIC REPOSITORY]
    return Card(
      color: Colors.black45,
      elevation: 4,
      child: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            const Text(
              "DIGITAL TWIN: ASSET SYNTHESIS",
              style: TextStyle(color: Colors.tealAccent, fontSize: 18, fontWeight: FontWeight.bold, letterSpacing: 1.2),
            ),
            const SizedBox(height: 20),
            Row(
              mainAxisAlignment: MainAxisAlignment.spaceAround,
              children: [
                _buildTelemetryDial("DRONE GLI", "[REDACTED]", Colors.lightGreenAccent),
                _buildTelemetryDial("SOIL VWC", "[REDACTED]", Colors.blueAccent),
                _buildTelemetryDial("HEALTH IDX", "[REDACTED]", Colors.green),
              ],
            ),
          ],
        ),
      ),
    );
  }

  Widget _buildTelemetryDial(String label, String value, Color color) {
    return Column(
      children: [
        Text(label, style: const TextStyle(color: Colors.grey, fontSize: 12, fontWeight: FontWeight.bold)),
        const SizedBox(height: 8),
        Text(value, style: TextStyle(color: color, fontSize: 24, fontWeight: FontWeight.bold, fontFamily: 'monospace')),
      ],
    );
  }
}
