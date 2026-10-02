# programbench/gnuplot_1776_gnuplot.a1bafa4:task_v6
# Full build environment (maintainers only, never shown to agents): cleanroom image plus the
# upstream source tree and a reference build at /opt/reference. Build context: repository root.
FROM programbench/gnuplot_1776_gnuplot.a1bafa4:task_cleanroom_v6
COPY sources/gnuplot__gnuplot.a1bafa4/ /opt/source/
RUN /opt/source/build.sh && cp /opt/source/bin/gnuplot /opt/reference-gnuplot
WORKDIR /workspace
