import 'package:flutter/material.dart';

class MissionControlPanel extends StatefulWidget {
  const MissionControlPanel({Key? key}) : super(key: key);

  @override
  _MissionControlPanelState createState() => _MissionControlPanelState();
}

class _MissionControlPanelState extends State<MissionControlPanel> {
  final bool _isExecuting = false;
  final String _missionLog = "Awaiting command input...";

  Future<void> _launchMission(bool isDryRun) async {
    // [INTERNAL API ROUTING AND PAYLOAD CONSTRUCTION REDACTED FOR PUBLIC REPOSITORY]
  }

  @override
  Widget build(BuildContext context) {
    return Card(
      color: Colors.black45,
      elevation: 4,
      child: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            const Text(
              "TACTICAL DRONE DEPLOYMENT",
              style: TextStyle(color: Colors.tealAccent, fontSize: 18, fontWeight: FontWeight.bold, letterSpacing: 1.2),
            ),
            const SizedBox(height: 20),
            Row(
              mainAxisAlignment: MainAxisAlignment.spaceEvenly,
              children: [
                ElevatedButton.icon(
                  icon: const Icon(Icons.science),
                  label: const Text("DRY RUN SIMULATION"),
                  style: ElevatedButton.styleFrom(backgroundColor: Colors.blueGrey),
                  onPressed: _isExecuting ? null : () => _launchMission(true),
                ),
                ElevatedButton.icon(
                  icon: const Icon(Icons.flight_takeoff),
                  label: const Text("AUTHORIZE LIVE LAUNCH"),
                  style: ElevatedButton.styleFrom(backgroundColor: Colors.redAccent),
                  onPressed: _isExecuting ? null : () => _launchMission(false),
                ),
              ],
            ),
            const SizedBox(height: 20),
            Container(
              width: double.infinity,
              padding: const EdgeInsets.all(12),
              color: Colors.black,
              child: Text(
                "> \",
                style: const TextStyle(color: Colors.greenAccent, fontFamily: 'monospace'),
              ),
            ),
          ],
        ),
      ),
    );
  }
}
